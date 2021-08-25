from datetime import date
import datetime
year = int(input("Introduzca su año de nacimiento: "))
month = int(input("Introduzca su mes de nacimiento. ej. Agosto = 8: "))
day = int(input("Introduzca su día de nacimiento: "))
currentTime = datetime.datetime.now()
currentArray = [currentTime.year, currentTime.month, currentTime.day]
birthDate = (year, month, day)
myDate = [e1 - e2 for e1, e2 in zip(currentArray,birthDate)]
print("Tienes", myDate[0], "años,", myDate[1], "meses y", myDate[2], "días")
