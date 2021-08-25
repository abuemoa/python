from datetime import date
year = int(input("Introduzca su año de nacimiento: "))
month = int(input("Introduzca su mes de nacimiento. ej. Agosto = 8: "))
day = int(input("Introduzca su día de nacimiento: "))
currentDate = (2021, 8, 25)
birthDate = (year, month, day)
myDate = [e1 - e2 for e1, e2 in zip(currentDate,birthDate)]
print(myDate)
