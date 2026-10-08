texto = "Ronald"
metodo = "upperrr"
metodo_reserva = "lower"
if hasattr(texto, metodo):
    print(getattr(texto, metodo)())
else:
    print("Não existe ometdo")    