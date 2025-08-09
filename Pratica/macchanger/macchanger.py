import subprocess

class MacChanger:
    def __init__(self):
        self.interface = input("Digite sua interface de rede: ").strip()
        self.novo_mac = input("Digite seu novo MAC address: ").strip()

    def mostrar_mac(self):
        """Mostra o MAC atual da interface"""
        subprocess.run(["ip", "link", "show", self.interface], check=True)

    def alterar_mac(self):
        try:
            print(f"[INFO] Derrubando interface {self.interface}...")
            subprocess.run(["ip", "link", "set", "dev", self.interface, "down"], check=True)

            print(f"[INFO] Alterando MAC para {self.novo_mac}...")
            subprocess.run(["ip", "link", "set", "dev", self.interface, "address", self.novo_mac], check=True)

            print(f"[INFO] Subindo interface {self.interface}...")
            subprocess.run(["ip", "link", "set", "dev", self.interface, "up"], check=True)

            print("[OK] MAC alterado com sucesso!")
            self.mostrar_mac()

        except subprocess.CalledProcessError as e:
            print(f"[ERRO] Falha ao executar comando: {e}")
        except Exception as e:
            print(f"[ERRO] Erro inesperado: {e}")

if __name__ == "__main__":
    mac = MacChanger()

    print("\n[INFO] MAC atual:")
    mac.mostrar_mac()

    print("\n[INFO] Alterando MAC...\n")
    mac.alterar_mac()
