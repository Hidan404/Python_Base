f1 = "AAACTBF"
f2 = "CTB"
f3 = ""

pos = f1.find(f2)
print(pos)

if pos != -1:
    print(f"A substring '{f2}' encontrada na posição {f3} da string '{f1}'")
    f3 = f1[pos:pos+len(f2)]
    print(f3)
else:
    print(f"A substring '{f2}' não foi encontrada na string '{f1}'")
    print(f3)