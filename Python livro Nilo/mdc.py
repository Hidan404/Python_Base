def mdc(n1, n2):
    if n1 <= 0 and n2 <= 0:
        return 0
    while n2 != 0:
        n1, n2 = abs(n2), abs(n1) % n2

    return n1    

def mmc(n1, n2):
    if n1 <= 0 or n2 <= 0:
        return 0
    return abs(n1 * n2) // mdc(n1, n2)            
    

print(mdc(12, 18))
print(mmc(12, 18))    