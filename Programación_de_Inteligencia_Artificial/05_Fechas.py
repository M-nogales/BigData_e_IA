from datetime import datetime
from datetime import date
from datetime import timedelta

now = datetime.now()
print('now: ', now)

def imp_date(fecha):
    print("Día: ", fecha.day)
    print("Mes: ", fecha.month)
    print("Año: ", fecha.year)

imp_date(now)

today = date.today()
print('Today: ', today)

def format_exit(fecha):
    return fecha.strftime("%d/%m/%Y")

print(format_exit(today))

dia = date(2024,1,1)
print(format_exit(dia))

def sum_days(fecha, dias):
    new_date = fecha + timedelta(days = dias)
    return new_date

print("sum_days 01/01/2024 + 55 dias",sum_days(dia,55))
fecha2 = sum_days(dia,55)

def comp_dates(f1,f2):
    result = f1-f2
    # return result
    return result.days

print(comp_dates(fecha2,dia))

def transform_string_date(str):
    fecha = datetime.strptime(str,"%d/%m/%Y")
    return fecha.date()

print(transform_string_date("01/01/2024"))