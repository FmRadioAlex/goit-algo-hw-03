import os 
from datetime import datetime as dtdt



def get_upcoming_birthdays(users):
    tdate=dtdt.today().date()
    tdate.toordinal()
    birthday=[]
    for user in users:
        bdate=user["birthday"]
        bdate=str(tdate.year)+bdate[4:]
        bdate=dtdt.strptime(bdate,"%Y.%m.%d").date()
        week_day=bdate.isoweekday()
        bdo=bdate.toordinal()
        days_between=bdo-tdate.toordinal()
        if 0<=days_between<7:
            if week_day<6:
                birthday.append({'name':user['name'],'birthday':dtdt.isoformat().replace('-','.')})
            elif dtdt.fromordinal(bdo+1).weekday()==0:
                birthday.append({'name':user['name'],'birthday':dtdt.fromordinal(bdo+1).isoformat().replace('-','.')[:10]})
            elif dtdt.fromordinal(bdo+2).weekday()==0:
                birthday.append({'name':user['name'],'birthday':dtdt.fromordinal(bdo+2).isoformat().replace('-','.')[:10]})

    return birthday


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.28"},
 
]
os.system('cls')
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)