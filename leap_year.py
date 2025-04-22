def leap_year():
    def leap_year():
    Year = int(input("Ingrese un año: "))
    if Year % 4 == 0 and Year % 100 != 0 or (Year % 400 == 0):
        print (f"El año {Year} es bisiesto")
    else:
        print (f"El año {Year} no es bisiesto")
