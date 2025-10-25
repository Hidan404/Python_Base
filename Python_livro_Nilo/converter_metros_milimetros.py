def metros_to_milimetros(valor):
    try:
        valor = valor * 100
        return f"Sua altura em centimetors  {valor}"
    except Exception as e:
        return f"Valor invalido"

print(metros_to_milimetros(1.61))