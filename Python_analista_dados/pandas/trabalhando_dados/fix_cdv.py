import csv
import re
from pathlib import Path

input_file = Path(__file__).parent.resolve() / "reviews.csv"        # nome do arquivo original
output_file = Path(__file__).parent.resolve() / "reviews_fixed.csv"   # nome do arquivo corrigido

# Expressão regular para dividir os 9 campos, respeitando aspas
# Como o separador é vírgula, mas o reviewText pode conter vírgulas,
# usamos um parser simples que lê campo a campo.

def parse_line(line):
    # Remove quebras de linha internas (substitui por espaço)
    line = line.rstrip('\n')
    fields = []
    current = ""
    in_quotes = False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '"':
            if in_quotes and i+1 < len(line) and line[i+1] == '"':
                # Aspas duplas escapadas - preserva uma aspa
                current += '"'
                i += 2
                continue
            else:
                in_quotes = not in_quotes
                i += 1
                continue
        if ch == ',' and not in_quotes:
            # Fim de campo
            fields.append(current)
            current = ""
            i += 1
            continue
        current += ch
        i += 1
    fields.append(current)  # último campo
    # Se o número de campos for menor que 9, pode ter quebras de linha não tratadas
    # Nesse caso, juntamos os campos extras no reviewText (campo índice 3)
    if len(fields) < 9:
        # Pode ocorrer se houver vírgulas dentro do reviewText sem aspas
        # Vamos concatenar tudo a partir do índice 3 até o penúltimo
        # Mas é melhor garantir que o reviewText esteja sempre entre aspas
        # Vamos simplesmente pegar os primeiros 3 campos e os últimos 5, e o meio é o reviewText
        # Como é um caso raro, tratamos manualmente.
        pass
    return fields

def fix_csv():
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Cabeçalho
    header = ["reviewerID","asin","reviewerName","reviewText",
              "unixReviewTime","reviewTime","day_diff","helpful_yes","total_vote"]

    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile, quoting=csv.QUOTE_ALL, escapechar='\\')
        writer.writerow(header)

        for line in lines[1:]:  # pula cabeçalho original
            if not line.strip():
                continue
            # Remove quebras de linha internas (substitui por espaço)
            line = line.replace('\n', ' ').replace('\r', '')
            # Usa o parser manual
            fields = parse_line(line)
            # Se o número de campos não for 9, tenta corrigir juntando campos extras
            if len(fields) != 9:
                # Se tiver mais, os primeiros 3 e últimos 5 são fixos, o resto é reviewText
                if len(fields) > 9:
                    # Junta os campos do índice 3 até (len-5) como reviewText
                    review_text = ' '.join(fields[3:-5])
                    new_fields = fields[:3] + [review_text] + fields[-5:]
                    fields = new_fields
                else:
                    # Se tiver menos, preenche com vazio (improvável)
                    while len(fields) < 9:
                        fields.append('')
            # Limpa espaços extras e escapa aspas internas
            # O writer fará o escape automaticamente com QUOTE_ALL
            writer.writerow(fields)

    print(f"Arquivo corrigido salvo como: {output_file}")

if __name__ == "__main__":
    fix_csv()