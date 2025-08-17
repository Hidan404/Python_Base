def salario_aumento(salario):

    try:
        salario = float(salario)

        if salario > 1250:
            salario+= salario * 0.10
            return salario

        salario+= salario * 0.10
        return salario    
    except Exception as e:
        return e

print(salario_aumento(1251))            