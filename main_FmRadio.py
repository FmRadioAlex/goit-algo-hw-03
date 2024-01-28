from datetime import datetime as dt
import os

def get_days_from_today(date):
    date= dt.date(date)                                 #Після отримання данних ми беремо тільки дату
    today=dt.date(dt.today())                           #Беремо теперешню дату та тільки дату(без часу) через .date()
    print(f'Дата яку ми ввели:\n{date}\n')
    print(f'Поточна дата:\n{today}\n')
    print(f'Різниця по дням: \n{(today-date).days}')
    return today-date                                   #просто віднімаєо дату на дату та повретаємо назад 
    


def start_main_program():                               #Функція ввода данних
    try:

        #input_time=dt(year=2024, month=1, day=6)       #вводим постійну дату (щоб не вводити кожен раз з початку дату)
        
        input_time=dt(year=int(input("Year= ")),month=int(input("Month= ")),day=int(input("Day= "))) #Вводимо дату яку ми хочемо

        #відправляємо данні які ми ввели в іншу функцію
        print(f'Різниця кількістю днів між заданою датою і поточною датою: \n{get_days_from_today(input_time)}\n') #виклкиаєем функцію на 4 строчці
            

    except Exception as eror:
        os.system('cls')
        print(f"Error: {eror}")
        start_main_program()

 
os.system('cls')                                        #Початок программи чистим термінал
start_main_program()                                    #викликаємо функцію (14 строчка)