print("Comienzo")
print("Introduzca la función factorial que quiere realizar")
operador = int(input())
print(f"Ha elegido el número {operador}")
numero = operador
if numero == 0:
    operador = 1
else:
    for i in range(1,operador):
        operador *= i

print(f"El resultado de la función factorial de {numero} es {operador}")                                                                        
