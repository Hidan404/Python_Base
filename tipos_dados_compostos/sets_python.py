conjuntoA = {1,2,3,4,5}
conjuntoB = set((3,6,7,8,9, 1))
print(conjuntoA.intersection(conjuntoB),conjuntoA.union(conjuntoB))
print(conjuntoA.difference(conjuntoB),type(conjuntoA))

print("*" * 20)
print(conjuntoA.symmetric_difference(conjuntoB))

fruta = set("banana")
print(fruta)