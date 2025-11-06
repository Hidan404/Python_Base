from datetime import datetime, timedelta

agora = datetime.now()
print(agora)


print(type(agora.isoformat()))

data = agora.isoformat().split("T")[0]

print(data)

data_formatada = agora.date().strftime("%d/%m/%y")
print(data_formatada)
print(type(data_formatada))


futuro_10_dias = timedelta(days=10)
agora+= futuro_10_dias
print(agora)