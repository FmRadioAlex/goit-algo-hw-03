from datetime import datetime as dt
import os

def get_days_from_today(date):

    today=dt.today()
    return

def start_main_program():
    try:
        input_time = dt(input("Ведіть дату 'РРРР-ММ-ДД'(2010,10,09): "))
        print(input_time)
    except Exception as eror:
        os.system('cls')
        print(f"Error: {eror}")
        start_main_program()

start_main_program()









