#!/usr/bin/env python3
"""
RTSP Camera Scanner via Tor - Para pentesters autorizados
Uso: python3 rtsp_tor_scanner.py [opções]
"""

import socket
import socks
import threading
import time
import ipaddress
import random
import logging
import json
import base64
import hashlib
from queue import Queue
from datetime import datetime
import requests
import stem
import stem.connection
import stem.process
from stem import Signal
from stem.control import Controller
import os
import sys

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rtsp_tor_scan.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TorRTSPScanner:
    def __init__(self, num_threads=50, timeout=5, tor_port=9050, tor_control_port=9051, tor_password=None):
        """
        Scanner RTSP via Tor com proteção de anonimato
        
        Args:
            num_threads: Número de threads (via Tor)
            timeout: Timeout em segundos
            tor_port: Porta SOCKS do Tor (padrão 9050)
            tor_control_port: Porta de controle do Tor (padrão 9051)
            tor_password: Senha do Tor (se houver)
        """
        self.num_threads = num_threads
        self.timeout = timeout
        self.tor_port = tor_port
        self.tor_control_port = tor_control_port
        self.tor_password = tor_password
        self.queue = Queue()
        self.results = []
        self.lock = threading.Lock()
        self.stop_flag = False
        self.scanned = 0
        self.open_ports = 0
        self.current_ip = None  # Para verificar mudança de IP
        
        # Configura socket padrão para usar Tor (SOCKS5)
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", self.tor_port)
        socket.socket = socks.socksocket
        
        # Verifica conexão com Tor
        self.check_tor_connection()
        
        # Obtém IP atual via Tor
        self.update_tor_ip()

    def check_tor_connection(self):
        """Verifica se o Tor está rodando e conectado"""
        try:
            # Testa se o Tor está respondendo via SOCKS
            test_sock = socks.socksocket()
            test_sock.set_proxy(socks.SOCKS5, "127.0.0.1", self.tor_port)
            test_sock.settimeout(5)
            test_sock.connect(("check.torproject.org", 80))
            test_sock.send(b"GET / HTTP/1.0\r\nHost: check.torproject.org\r\n\r\n")
            response = test_sock.recv(1024)
            test_sock.close()
            
            if b"Tor" in response:
                logger.info("✅ Tor está rodando e respondendo")
            else:
                logger.warning("⚠️  Tor pode não estar funcionando corretamente")
                
            # Tenta conectar ao controlador
            try:
                with Controller.from_port(port=self.tor_control_port) as controller:
                    controller.authenticate(password=self.tor_password)
                    logger.info("✅ Conexão com controlador Tor estabelecida")
            except Exception as e:
                logger.warning(f"⚠️  Não foi possível conectar ao controlador Tor: {e}")
                
        except Exception as e:
            logger.error(f"❌ Erro ao conectar ao Tor: {e}")
            logger.error("Certifique-se que o Tor está rodando (sudo systemctl start tor)")
            sys.exit(1)

    def update_tor_ip(self):
        """Obtém o IP atual via Tor"""
        try:
            test_sock = socks.socksocket()
            test_sock.set_proxy(socks.SOCKS5, "127.0.0.1", self.tor_port)
            test_sock.settimeout(10)
            test_sock.connect(("api.ipify.org", 80))
            test_sock.send(b"GET / HTTP/1.0\r\nHost: api.ipify.org\r\n\r\n")
            response = test_sock.recv(1024).decode()
            test_sock.close()
            
            # Extrai IP da resposta
            ip_start = response.find("\r\n\r\n") + 4
            ip = response[ip_start:].strip()
            if ip:
                self.current_ip = ip
                logger.info(f"🌐 IP via Tor: {self.current_ip}")
            else:
                logger.warning("Não foi possível obter IP via Tor")
        except Exception as e:
            logger.error(f"Erro ao obter IP via Tor: {e}")

    def renew_tor_circuit(self):
        """Renova o circuito Tor para mudar o IP de saída"""
        try:
            with Controller.from_port(port=self.tor_control_port) as controller:
                controller.authenticate(password=self.tor_password)
                controller.signal(Signal.NEWNYM)
                time.sleep(1)  # Aguarda novo circuito
                self.update_tor_ip()
                logger.info("🔄 Circuito Tor renovado")
        except Exception as e:
            logger.error(f"Erro ao renovar circuito Tor: {e}")

    def is_public_ip(self, ip):
        """Verifica se o IP é público"""
        try:
            ip_obj = ipaddress.ip_address(ip)
            return not (
                ip_obj.is_private or
                ip_obj.is_multicast or
                ip_obj.is_loopback or
                ip_obj.is_unspecified or
                ip_obj.is_reserved
            )
        except:
            return False

    def test_rtsp_connection(self, ip, port=554):
        """
        Testa conexão RTSP via Tor
        
        Args:
            ip: Endereço IP
            port: Porta
        
        Returns:
            tuple: (ip, status, info)
        """
        try:
            # Usa socket via Tor (já configurado globalmente)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            # Conecta via Tor
            sock.connect((ip, port))
            
            # Envia OPTIONS para identificar RTSP
            request = f"OPTIONS rtsp://{ip}:{port}/ RTSP/1.0\r\nCSeq: 1\r\nUser-Agent: RTSP-Tor-Scanner\r\n\r\n"
            sock.send(request.encode())
            
            response = sock.recv(2048).decode('utf-8', errors='ignore')
            sock.close()
            
            with self.lock:
                self.scanned += 1
            
            if 'RTSP/1.0' in response:
                with self.lock:
                    self.open_ports += 1
                    logger.info(f"🔓 RTSP ABERTO via Tor: {ip}:{port}")
                
                # Extrai informações
                info = {'service': 'RTSP'}
                for line in response.split('\n'):
                    if 'Server:' in line:
                        info['server'] = line.split(':', 1)[1].strip()
                    if '401 Unauthorized' in response:
                        info['auth_required'] = True
                
                # Tenta descobrir streams
                streams = self.find_streams(ip, port)
                if streams:
                    info['streams'] = streams
                
                return (ip, 'OPEN', info)
            else:
                return (ip, 'CLOSED', None)
                
        except socket.timeout:
            return (ip, 'TIMEOUT', None)
        except ConnectionRefusedError:
            return (ip, 'CLOSED', None)
        except Exception as e:
            return (ip, 'ERROR', str(e))

    def find_streams(self, ip, port):
        """Tenta encontrar streams RTSP via Tor"""
        streams = []
        common_paths = [
            '/stream', '/live', '/h264', '/h265', '/video',
            '/cam', '/camera', '/stream1', '/stream2',
            '/main', '/sub', '/ch1', '/ch2',
            '/rtsp', '/unicast', '/multicast',
            '/', '/live.sdp', '/stream.sdp'
        ]
        
        for path in common_paths[:5]:  # Limita para não sobrecarregar
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                sock.connect((ip, port))
                
                request = f"DESCRIBE rtsp://{ip}:{port}{path} RTSP/1.0\r\nCSeq: 2\r\n\r\n"
                sock.send(request.encode())
                response = sock.recv(1024).decode('utf-8', errors='ignore')
                sock.close()
                
                if '200 OK' in response and 'RTSP/1.0' in response:
                    stream_url = f"rtsp://{ip}:{port}{path}"
                    streams.append(stream_url)
                    logger.info(f"📹 Stream via Tor encontrada: {stream_url}")
                    
            except Exception:
                continue
        
        return streams

    def save_result(self, result, encrypted=False, key=None):
        """
        Salva resultado em arquivo (opcionalmente criptografado)
        
        Args:
            result: (ip, status, info)
            encrypted: Se True, criptografa com AES simples (base64)
            key: Chave para criptografia (se None, usa hash do IP)
        """
        ip, status, info = result
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        entry = {
            'timestamp': timestamp,
            'ip': ip,
            'port': 554,
            'status': status,
            'info': info
        }
        
        json_entry = json.dumps(entry, indent=2)
        
        if encrypted:
            # Criptografia simples (para demonstração)
            if key is None:
                key = hashlib.sha256(ip.encode()).hexdigest()[:16]
            # XOR com chave (exemplo, não é criptografia forte)
            key_bytes = key.encode()
            data = json_entry.encode()
            encrypted_data = bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])
            encrypted_b64 = base64.b64encode(encrypted_data).decode()
            
            filename = f"rtsp_results_{datetime.now().strftime('%Y%m%d')}.enc"
            with open(filename, 'a') as f:
                f.write(encrypted_b64 + '\n')
        else:
            filename = f"rtsp_results_{datetime.now().strftime('%Y%m%d')}.txt"
            with open(filename, 'a') as f:
                f.write(f"=== {timestamp} ===\n")
                f.write(f"IP: {ip}\n")
                f.write(f"Port: 554\n")
                f.write(f"Status: {status}\n")
                if info:
                    for k, v in info.items():
                        f.write(f"{k}: {v}\n")
                f.write("-" * 50 + "\n\n")

    def worker(self):
        """Worker thread com renovação periódica de circuito"""
        renew_counter = 0
        while not self.stop_flag:
            try:
                ip = self.queue.get(timeout=2)
                if ip is None:
                    break
                
                # Renova circuito a cada 100 IPs (para evitar detecção)
                renew_counter += 1
                if renew_counter >= 100:
                    self.renew_tor_circuit()
                    renew_counter = 0
                
                # Verifica se é público
                if not self.is_public_ip(ip):
                    self.queue.task_done()
                    continue
                
                result = self.test_rtsp_connection(ip)
                
                if result[1] == 'OPEN':
                    with self.lock:
                        self.results.append(result)
                        self.save_result(result, encrypted=False)  # Pode ativar criptografia
                
                self.queue.task_done()
                
            except Exception as e:
                if not self.stop_flag:
                    logger.error(f"Erro no worker: {str(e)}")
                self.queue.task_done()

    def scan_random_public_ips(self, count=10000, port=554):
        """Escaneia IPs públicos aleatórios via Tor"""
        logger.info("=" * 60)
        logger.info(f"🔍 Scan de {count} IPs públicos via Tor")
        logger.info(f"🌐 IP de saída: {self.current_ip}")
        logger.info("=" * 60)
        
        # Gera IPs aleatórios
        generated = 0
        while generated < count:
            ip = f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            if self.is_public_ip(ip):
                self.queue.put(ip)
                generated += 1
                if generated % 1000 == 0:
                    logger.info(f"📊 {generated} IPs enfileirados...")
        
        # Inicia threads
        threads = []
        for i in range(self.num_threads):
            t = threading.Thread(target=self.worker, name=f"TorWorker-{i}")
            t.daemon = True
            t.start()
            threads.append(t)
        
        # Monitora progresso
        start_time = time.time()
        while not self.queue.empty():
            time.sleep(5)
            with self.lock:
                logger.info(f"📊 Escaneados: {self.scanned}/{count} | Abertos: {self.open_ports}")
        
        self.queue.join()
        self.stop_flag = True
        
        for _ in range(self.num_threads):
            self.queue.put(None)
        
        for t in threads:
            t.join(timeout=2)
        
        elapsed = time.time() - start_time
        logger.info("=" * 60)
        logger.info(f"✅ Scan concluído em {elapsed:.1f}s")
        logger.info(f"📊 IPs escaneados: {self.scanned}")
        logger.info(f"🔓 Portas abertas: {self.open_ports}")
        logger.info(f"📁 Resultados salvos em rtsp_results_{datetime.now().strftime('%Y%m%d')}.txt")
        logger.info("=" * 60)

    def scan_specific_blocks(self, blocks, port=554):
        """Escaneia blocos específicos via Tor"""
        logger.info(f"Escaneando {len(blocks)} blocos via Tor")
        
        for block in blocks:
            try:
                network = ipaddress.ip_network(block, strict=False)
                logger.info(f"Adicionando {block} ({network.num_addresses} IPs)")
                for ip in network.hosts():
                    if self.is_public_ip(str(ip)):
                        self.queue.put(str(ip))
            except Exception as e:
                logger.error(f"Erro no bloco {block}: {e}")
        
        # Inicia workers (mesmo padrão)
        threads = []
        for i in range(self.num_threads):
            t = threading.Thread(target=self.worker, name=f"TorWorker-{i}")
            t.daemon = True
            t.start()
            threads.append(t)
        
        self.queue.join()
        self.stop_flag = True
        for _ in range(self.num_threads):
            self.queue.put(None)
        for t in threads:
            t.join(timeout=2)
        
        logger.info(f"✅ Scan concluído. Encontrados {self.open_ports} IPs com RTSP")

def main():
    """Função principal"""
    print("=" * 70)
    print("🌐 RTSP SCANNER VIA TOR - PARA PENTESTERS AUTORIZADOS")
    print("🔍 Porta 554 - Câmeras IP")
    print("=" * 70)
    print("\n⚠️  AVISO LEGAL:")
    print("=" * 70)
    
    # Verifica se Tor está instalado
    try:
        import stem
    except ImportError:
        print("❌ Stem não instalado. Execute: pip install stem requests[socks] PySocks")
        sys.exit(1)
    
    print("\nOpções:")
    print("1 - Escanear IPs aleatórios (via Tor)")
    print("2 - Escanear blocos específicos (via Tor)")
    print("3 - Sair")
    
    choice = input("\nEscolha: ").strip()
    
    if choice == '1':
        count = int(input("Número de IPs a escanear (padrão 10000): ") or "10000")
        threads = int(input("Número de threads (padrão 50): ") or "50")
        timeout = int(input("Timeout em segundos (padrão 5): ") or "5")
        
        scanner = TorRTSPScanner(num_threads=threads, timeout=timeout)
        scanner.scan_random_public_ips(count=count)
        
    elif choice == '2':
        blocks_input = input("Digite os blocos (ex: 8.8.8.0/24,1.1.1.0/24): ").strip()
        blocks = [b.strip() for b in blocks_input.split(',')]
        threads = int(input("Número de threads (padrão 50): ") or "50")
        timeout = int(input("Timeout em segundos (padrão 5): ") or "5")
        
        scanner = TorRTSPScanner(num_threads=threads, timeout=timeout)
        scanner.scan_specific_blocks(blocks)
        
    elif choice == '3':
        print("Saindo...")
        sys.exit(0)
    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()