import sys
import itertools

def imprime_bytes(imagem, bytes_por_linha=16):
    for b in itertools.batched(imagem, bytes_por_linha):
        hex_visualização = " ".join([f"{v:02x}" for v in b])
        tvisualizacao = " ".join([chr(v) if chr(v).isprintable() else "." for v in b])
        print(f"{hex_visualização} {" " * 3 * (bytes_por_linha - len(b))} {tvisualizacao}")

def executar():
    with open(sys.argv[1], "rb") as f:
        imagem = f.read()
    imprime_bytes(imagem)     

if __name__ == "__main__":
    executar()           