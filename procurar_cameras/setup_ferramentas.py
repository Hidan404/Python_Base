#!/usr/bin/env python3
"""
Script de setup multi-distro para ambiente de desenvolvimento e hacking.
Suporta: Arch Linux (CachyOS), Fedora, Debian/Ubuntu.
Instala as melhores ferramentas por categoria, evitando redundâncias.
"""

import subprocess
import sys
import os
import shutil
import platform
from typing import List, Tuple, Dict, Optional

# ============================================================
# CORES PARA OUTPUT
# ============================================================
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_step(msg: str) -> None:
    print(f"\n{Colors.BLUE}{Colors.BOLD}==> {msg}{Colors.END}")

def print_success(msg: str) -> None:
    print(f"{Colors.GREEN}✓ {msg}{Colors.END}")

def print_error(msg: str) -> None:
    print(f"{Colors.RED}✗ {msg}{Colors.END}")

def print_info(msg: str) -> None:
    print(f"{Colors.YELLOW}ℹ {msg}{Colors.END}")

# ============================================================
# DETECÇÃO DA DISTRIBUIÇÃO
# ============================================================
class Distro:
    def __init__(self):
        self.id = None
        self.name = None
        self.pkg_manager = None
        self.install_cmd = None
        self.update_cmd = None
        self.detect()

    def detect(self):
        """Detecta a distribuição via /etc/os-release."""
        try:
            with open("/etc/os-release") as f:
                data = {}
                for line in f:
                    if "=" in line:
                        key, val = line.strip().split("=", 1)
                        data[key] = val.strip('"')
            self.id = data.get("ID", "").lower()
            self.name = data.get("NAME", "")
        except FileNotFoundError:
            # fallback
            self.id = "unknown"

        if self.id in ["arch", "cachyos"]:
            self.pkg_manager = "pacman"
            self.install_cmd = ["sudo", "pacman", "-S", "--needed", "--noconfirm"]
            self.update_cmd = ["sudo", "pacman", "-Sy"]
        elif self.id in ["fedora"]:
            self.pkg_manager = "dnf"
            self.install_cmd = ["sudo", "dnf", "install", "-y"]
            self.update_cmd = ["sudo", "dnf", "check-update"]
        elif self.id in ["debian", "ubuntu", "pop", "linuxmint"]:
            self.pkg_manager = "apt"
            self.install_cmd = ["sudo", "apt", "install", "-y"]
            self.update_cmd = ["sudo", "apt", "update"]
        else:
            print_error(f"Distribuição não suportada: {self.id}")
            sys.exit(1)

        print_info(f"Distro detectada: {self.name} ({self.id}) - Gerenciador: {self.pkg_manager}")

distro = Distro()

# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================
def run_cmd(cmd: List[str], check: bool = True, capture: bool = False) -> Tuple[int, str]:
    print_info(f"Executando: {' '.join(cmd)}")
    try:
        if capture:
            result = subprocess.run(cmd, capture_output=True, text=True, check=check)
            return result.returncode, result.stdout.strip()
        else:
            subprocess.run(cmd, check=check)
            return 0, ""
    except subprocess.CalledProcessError as e:
        print_error(f"Comando falhou com código {e.returncode}")
        return e.returncode, e.stderr if hasattr(e, 'stderr') else ""

def check_command_exists(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def is_package_installed(pkg: str) -> bool:
    """Verifica se o pacote está instalado de acordo com o gerenciador."""
    if distro.pkg_manager == "pacman":
        code, _ = run_cmd(["pacman", "-Q", pkg], check=False, capture=True)
        return code == 0
    elif distro.pkg_manager == "dnf":
        code, _ = run_cmd(["dnf", "list", "installed", pkg], check=False, capture=True)
        return code == 0
    elif distro.pkg_manager == "apt":
        code, _ = run_cmd(["dpkg", "-s", pkg], check=False, capture=True)
        return code == 0 and "Status: install ok installed" in _
    return False

def install_packages(packages: List[str]) -> None:
    """Instala uma lista de pacotes usando o gerenciador apropriado."""
    if not packages:
        return
    to_install = [p for p in packages if not is_package_installed(p)]
    if not to_install:
        print_info("Todos os pacotes já estão instalados.")
        return
    # Atualiza a lista de pacotes (excepto Arch que já tem -Sy)
    if distro.pkg_manager in ["dnf", "apt"]:
        run_cmd(distro.update_cmd, check=False)
    run_cmd(distro.install_cmd + to_install)

# ============================================================
# DEFINIÇÃO DE PACOTES POR CATEGORIA E DISTRO
# ============================================================
# Pacotes base (essenciais para desenvolvimento e sistema)
BASE_PKGS = {
    "arch": [
        "base-devel", "git", "wget", "curl", "unzip", "zip",
        "openssl", "zlib", "cmake", "gcc", "make",
        "python", "python-pip", "python-setuptools", "python-wheel",
        "python-build", "python-virtualenv",
        "nodejs", "npm",
        "bat", "ripgrep", "fd", "fzf", "jq", "yq",
        "tmux", "htop", "neofetch", "tree", "ncdu"
    ],
    "fedora": [
        "git", "wget", "curl", "unzip", "zip",
        "openssl", "zlib-devel", "cmake", "gcc", "make",
        "python3", "python3-pip", "python3-setuptools", "python3-wheel",
        "python3-build", "python3-virtualenv",
        "nodejs", "npm",
        "bat", "ripgrep", "fd-find", "fzf", "jq", "yq",
        "tmux", "htop", "neofetch", "tree", "ncdu"
    ],
    "debian": [
        "git", "wget", "curl", "unzip", "zip",
        "openssl", "zlib1g-dev", "cmake", "gcc", "make",
        "python3", "python3-pip", "python3-setuptools", "python3-wheel",
        "python3-build", "python3-virtualenv",
        "nodejs", "npm",
        "bat", "ripgrep", "fd-find", "fzf", "jq", "yq",
        "tmux", "htop", "neofetch", "tree", "ncdu"
    ]
}

# File managers TUI (apenas os melhores: Yazi e nnn)
FILE_MANAGERS = {
    "arch": ["yazi", "nnn"],
    "fedora": ["yazi", "nnn"],
    "debian": ["yazi", "nnn"]
}

# TUI extras (bottom e lazygit)
TUI_EXTRAS = {
    "arch": ["bottom", "lazygit"],
    "fedora": ["bottom", "lazygit"],
    "debian": ["bottom", "lazygit"]
}

# Ferramentas adicionais modernas (exa, zoxide, duf, etc.)
EXTRA_MODERN = {
    "arch": ["exa", "zoxide", "duf", "procs", "dust", "hyperfine"],
    "fedora": ["exa", "zoxide", "duf", "procs", "dust", "hyperfine"],
    "debian": ["exa", "zoxide", "duf", "procs", "dust", "hyperfine"]
}

# Ferramentas de hacking (15 por distro)
HACKING_TOOLS = {
    "arch": [
        "nmap", "wireshark-qt", "metasploit", "sqlmap", "hydra",
        "john", "aircrack-ng", "burpsuite", "nikto", "openvpn",
        "tcpdump", "netcat", "socat", "proxychains-ng", "tor"
    ],
    "fedora": [
        "nmap", "wireshark", "metasploit", "sqlmap", "hydra",
        "john", "aircrack-ng", "burpsuite", "nikto", "openvpn",
        "tcpdump", "netcat", "socat", "proxychains-ng", "tor"
    ],
    "debian": [
        "nmap", "wireshark", "metasploit", "sqlmap", "hydra",
        "john", "aircrack-ng", "burpsuite", "nikto", "openvpn",
        "tcpdump", "netcat", "socat", "proxychains-ng", "tor"
    ]
}

# ============================================================
# INSTALAÇÃO POR CATEGORIA
# ============================================================
def install_system_packages():
    print_step("Instalando pacotes base do sistema...")
    pkgs = BASE_PKGS.get(distro.id, BASE_PKGS["arch"])
    install_packages(pkgs)

def install_file_managers():
    print_step("Instalando gerenciadores de arquivos TUI (Yazi e nnn)...")
    pkgs = FILE_MANAGERS.get(distro.id, FILE_MANAGERS["arch"])
    install_packages(pkgs)

def install_tui_extras():
    print_step("Instalando TUI extras (bottom, lazygit)...")
    pkgs = TUI_EXTRAS.get(distro.id, TUI_EXTRAS["arch"])
    install_packages(pkgs)

def install_extra_modern_tools():
    print_step("Instalando ferramentas modernas (exa, zoxide, duf, ...)")
    pkgs = EXTRA_MODERN.get(distro.id, EXTRA_MODERN["arch"])
    install_packages(pkgs)

def install_hacking_tools():
    print_step("Instalando ferramentas de hacking (15 ferramentas)...")
    pkgs = HACKING_TOOLS.get(distro.id, HACKING_TOOLS["arch"])
    install_packages(pkgs)

# Ferramentas específicas para Python (Poetry, uv) – instaladas via script, não pacote
def install_poetry():
    print_step("Instalando Poetry...")
    if check_command_exists("poetry"):
        print_success("Poetry já está instalado.")
        return
    run_cmd(["curl", "-sSL", "https://install.python-poetry.org", "|", "python3", "-"], shell=True)
    # Adiciona ao PATH no ~/.bashrc ou ~/.zshrc (detecta shell)
    shell_rc = os.path.expanduser("~/.bashrc")
    if os.path.exists(os.path.expanduser("~/.zshrc")):
        shell_rc = os.path.expanduser("~/.zshrc")
    with open(shell_rc, "a") as f:
        f.write('\n# Poetry\nexport PATH="$HOME/.local/bin:$PATH"\n')
    print_success("Poetry instalado.")

def install_uv():
    print_step("Instalando uv...")
    if check_command_exists("uv"):
        print_success("uv já está instalado.")
        return
    run_cmd(["curl", "-LsSf", "https://astral.sh/uv/install.sh", "|", "sh"], shell=True)

def install_frontend_tools():
    print_step("Instalando ferramentas globais do frontend (yarn, pnpm, etc)...")
    if not check_command_exists("npm"):
        print_error("npm não encontrado. Instale Node.js primeiro.")
        return
    tools = ["yarn", "pnpm", "typescript", "ts-node", "eslint", "prettier", "live-server", "http-server", "nodemon"]
    for tool in tools:
        if check_command_exists(tool):
            print_success(f"{tool} já instalado.")
        else:
            run_cmd(["sudo", "npm", "install", "-g", tool])

def setup_git_aliases():
    print_step("Configurando aliases do Git...")
    aliases = {
        "st": "status",
        "co": "checkout",
        "br": "branch",
        "ci": "commit",
        "lg": "log --oneline --graph --decorate --all",
        "unstage": "reset HEAD --",
        "last": "log -1 HEAD",
        "visual": "!gitk"
    }
    for alias, cmd in aliases.items():
        run_cmd(["git", "config", "--global", f"alias.{alias}", cmd], check=False)
    run_cmd(["git", "config", "--global", "core.editor", "nano"], check=False)

def setup_shell():
    """Configura shell (Zsh ou Bash) com temas e plugins (se disponível)."""
    print_step("Configurando shell (Oh My Zsh ou bash-it)...")
    # Detecta se Zsh está disponível
    if check_command_exists("zsh"):
        # Instala Oh My Zsh se não existir
        if not os.path.exists(os.path.expanduser("~/.oh-my-zsh")):
            run_cmd(['sh', '-c', '$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)'], check=False)
        # Plugins
        plugins = ["zsh-autosuggestions", "zsh-syntax-highlighting"]
        for p in plugins:
            if distro.pkg_manager == "pacman" and not is_package_installed(p):
                install_packages([p])
            elif distro.pkg_manager in ["dnf", "apt"]:
                # Nomes podem variar, tentamos instalar
                pkg_name = p if distro.id == "arch" else f"zsh-{p}" if distro.id == "fedora" else f"zsh-{p}"
                if not is_package_installed(pkg_name):
                    install_packages([pkg_name])
        # Adiciona source no .zshrc
        zshrc = os.path.expanduser("~/.zshrc")
        if os.path.exists(zshrc):
            with open(zshrc, "r") as f:
                content = f.read()
            if "zsh-syntax-highlighting" not in content:
                with open(zshrc, "a") as f:
                    f.write('\n# Plugins\nsource /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh\n')
                    f.write('source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh\n')
    else:
        # Fallback para Bash com bash-it
        if not os.path.exists(os.path.expanduser("~/.bash_it")):
            run_cmd(['git', 'clone', '--depth=1', 'https://github.com/Bash-it/bash-it.git', '~/.bash_it'], shell=True)
            run_cmd(['~/.bash_it/install.sh'], shell=True)

# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================
def main():
    print(f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   🚀  SETUP MULTI-DISTRO - DEV + HACKING                   ║
║          Arch/CachyOS | Fedora | Debian/Ubuntu             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
    """)
    if os.geteuid() != 0:
        print_error("Este script precisa ser executado com sudo (ou como root).")
        print_info("Execute: sudo python3 setup_multi.py")
        sys.exit(1)

    print_info(f"Sistema detectado: {distro.name} ({distro.id})")
    print_info("Iniciando instalação...\n")

    # Executa as instalações
    install_system_packages()
    install_file_managers()
    install_tui_extras()
    install_extra_modern_tools()
    install_poetry()
    install_uv()
    install_frontend_tools()
    install_hacking_tools()
    setup_git_aliases()
    setup_shell()

    print(f"""
{Colors.GREEN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ✅  INSTALAÇÃO CONCLUÍDA COM SUCESSO!                     ║
║                                                              ║
║   Ferramentas instaladas:                                   ║
║   • Sistema base + Python, Node.js                         ║
║   • File managers: Yazi, nnn                               ║
║   • TUI extras: bottom, lazygit                            ║
║   • Modernos: exa, zoxide, duf, procs, dust, hyperfine    ║
║   • Frontend: yarn, pnpm, TypeScript, ESLint, Prettier    ║
║   • Hacking: 15 ferramentas (nmap, wireshark, etc.)       ║
║   • Git aliases configurados                               ║
║   • Shell configurado (Oh My Zsh ou bash-it)              ║
║                                                              ║
║   Após a instalação, recarregue o shell:                   ║
║   • Zsh: source ~/.zshrc                                   ║
║   • Bash: source ~/.bashrc                                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
    """)

if __name__ == "__main__":
    main()