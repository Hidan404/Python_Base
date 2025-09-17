def mdc(n1, n2):
    if n1 <= 0 and n2 <= 0:
        return 0
    while n2 != 0:
        n1, n2 = abs(n2), abs(n1) % n2

def mmc()        
    

print(mdc(0, 18))    