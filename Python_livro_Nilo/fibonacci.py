def fibonacci(n):
    if n <= 1:
        return n
    else:    
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(12))


def fibonaci_sem_recursao(n):
    if n <= 1:
        return n
        