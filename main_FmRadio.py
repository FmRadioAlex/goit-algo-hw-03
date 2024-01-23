from datetime import datetime as dt
import os

def get_days_from_today(date):
    date= dt.date(date)
    today=dt.date(dt.today())
    print(f'Дата яку ми ввели:\n{date}\n')
    print(f'Поточна дата:\n{today}\n')
    print(f'Різниця кількістю днів між заданою датою і поточною датою:\n{today-date}\n')
    


def start_main_program():
    try:

        input_time=dt(year=2024, month=1, day=6)
        #input_time = dt(year=int(input("Year= ")), month=int(input("Month= ")), day=int(input("Day= ")))
        get_days_from_today(input_time)
        

    except Exception as eror:
        os.system('cls')
        print(f"Error: {eror}")
        start_main_program()

os.system('cls')
start_main_program() 