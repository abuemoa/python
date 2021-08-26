import datetime
import time

year = int(input("Introduzca su año de nacimiento: "))
month = int(input("Introduzca su mes de nacimiento. ej. Agosto = 8: "))
day = int(input("Introduzca su día de nacimiento: "))

currentTime = time.time()
givenTime = datetime.datetime(year, month, day, 0, 0).timestamp()
difference = currentTime - givenTime

yearsOld = int((time.strftime('%Y', time.localtime(difference))))
MonthsOld = int((time.strftime('%m', time.localtime(difference))))
DaysOld = int((time.strftime('%d', time.localtime(difference))))

print("Tienes", (yearsOld - 1970), "años", MonthsOld - 1, "meses y", DaysOld - 1, "días")
