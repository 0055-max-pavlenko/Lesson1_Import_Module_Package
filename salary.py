import math

#В старой студенческой шутке, чтобы попросить зарплату у работадателя 
#нужно придумать ее величину и умножить на число "пи")))
def calculate_salary(name, imagined_salary):
    print(f'Начисленная зарплата для сотрудника {name} равна {math.ceil(math.pi*imagined_salary)} руб.')
