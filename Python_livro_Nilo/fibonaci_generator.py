def fibonaci(fim):
    p,s = 0,1
    while s < fim:
        yield s
        p, s = s, s + p


sequencia = [x for x in fibonaci(50)]
print(sequencia)