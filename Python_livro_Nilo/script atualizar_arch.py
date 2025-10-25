import subprocess


def atualizar_arch():
    try:
        comando = ["sudo", "pacman", "-Syu", "--noconfirm"]
        processo = subprocess.run(comando, capture_output=True, text=True)
        if processo.returncode == 0:
            print("Sistema atualizado com sucesso.")
            print(processo.stdout)
        else:
            print("Erro ao atualizar o sistema:")
            print(processo.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
    except subprocess.SubprocessError as e:
        print(f"Erro geral de subprocesso: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")                