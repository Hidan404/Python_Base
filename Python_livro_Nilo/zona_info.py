from datetime import datetime
from zoneinfo import ZoneInfo
import zoneinfo

for zona in sorted(zoneinfo.available_timezones()):
    print(zona)


# Hora atual em Tóquio
tz_tokyo = ZoneInfo("Asia/Tokyo")
agora_tokyo = datetime.now(tz=tz_tokyo)
print(f"Agora em Tóquio: {agora_tokyo}")


tz_parauapebas = ZoneInfo("America/Belem")
agora_paraupebas = datetime.now(tz=tz_parauapebas)
print(f"Agora em Parauapebas {agora_paraupebas} ")


#melhor metodo pegar IANA oficioal e usar zoneinfo