def all_seconds(dias=1,horas=1,minutos=1,segundos=1):
    try:
        dias = dias * 86400
        horas = horas * 3600
        minutos = minutos * 60
        segundos = segundos
        total = dias + horas + segundos
        print(total)
    except Exception as e:
        print(f"Erro: {e}")


all_seconds(2, 2, 50, 120)