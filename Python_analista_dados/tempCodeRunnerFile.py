
valor_emprerstimos = abrir_arquivo_passar_lista()
retorna_valor_emprestimos = map(lambda emp: emp["valor_emprestimos"], valor_emprerstimos)
print(list(retorna_valor_emprestimos))