from datetime import date
import datetime

year = int(input("Introduzca su año de nacimiento: "))
month = int(input("Introduzca su mes de nacimiento. ej. Agosto = 8: "))
day = int(input("Introduzca su día de nacimiento: "))
current_time = datetime.datetime.now()
current_array = [current_time.year, current_time.month, current_time.day]

birth_date = (year, month, day)
my_date = [e1 - e2 for e1, e2 in zip(current_array,birth_date)]

if (current_array[1] < month):
    my_date[1] += 12
    my_date[0] -= 1

print("Tienes", my_date[0], "años,", my_date[1], "meses y", my_date[2], "días"
