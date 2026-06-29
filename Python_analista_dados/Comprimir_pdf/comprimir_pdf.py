import sys
from pypdf import PdfReader, PdfWriter

def comprimir_pdf_pypdf(arquivo_entrada, arquivo_saida=None):
    if arquivo_saida is None:
        base, ext = arquivo_entrada.rsplit('.', 1)
        arquivo_saida = f"{base}_comprimido.pdf"

    leitor = PdfReader(arquivo_entrada)
    escritor = PdfWriter()

    # Adiciona todas as páginas (o escritor já vai comprimir ao salvar)
    for pagina in leitor.pages:
        escritor.add_page(pagina)

    # (Opcional) remover metadados para ganhar espaço
    escritor.add_metadata({})

    # Salva com compressão padrão
    with open(arquivo_saida, "wb") as f:
        escritor.write(f)

    print(f"Arquivo compactado salvo como: {arquivo_saida}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python comprimir_pdf.py [arquivo_entrada] [arquivo_saida_opcional]")
        sys.exit(1)
    entrada = sys.argv[1]
    saida = sys.argv[2] if len(sys.argv) > 2 else None
    comprimir_pdf_pypdf(entrada, saida)