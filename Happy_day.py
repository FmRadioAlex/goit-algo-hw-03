import os 
from datetime import datetime as dtdt
import datetime

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.30"}, 
]

def get_upcoming_birthdays():

    happy_day=[]
    for user in users: 
        day_birthday=dtdt.strptime(user['birthday'],'%Y.%m.%d').date()
        day_now=(dtdt.now()).date()
        day_happy=dtdt(day_now.year, day_birthday.month, day_birthday.day).date()
        if(day_happy-day_now).days < 0:
            day_happy=dtdt(day_now.year+1, day_birthday.month, day_birthday.day).date()
        elif(day_happy - day_now).days < 7:
            if(day_happy-day_now).days == 6:
                day_happy=day_happy+datetime.timedelta(days=1)
            elif(day_happy-day_now).days == 5:
                day_happy=day_happy+datetime.timedelta(days=2)
            list_congra={'Ім`я':user['name'], 'Коли треба привітати його':dtdt.strftime(day_happy,'%Y.%m.%d')}
            happy_day.append(list_congra)
    return happy_day

os.system('cls')
upcoming_birthdays = get_upcoming_birthdays()
print("Список привітань на цьому тижні:", upcoming_birthdays)