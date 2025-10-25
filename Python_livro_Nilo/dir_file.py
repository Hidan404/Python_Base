import os
import os.path

for d in os.listdir("."):
    if os.path.isdir(d):
        print(f"[DIR]  {d}")
    elif os.path.isfile(d):
        print(f"[FILE] {d}")    
    else:
        tamanho = os.path.getsize(d)
        print(f"[FILE] {d} - {tamanho} bytes")