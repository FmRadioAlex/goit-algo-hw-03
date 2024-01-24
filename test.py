import datetime
from datetime import datetime
def get_days_from_today(date=input("Input date Y-M-D: ")):
    date1 = datetime.strptime(date, "%Y-%m-%d")
    date_now = datetime.today()
    print((date1 - date_now).days)

get_days_from_today()