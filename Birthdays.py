# 18th Project: Birthdays
# Purpose: To practice datetime module
# TIL: str.split("seperator") -> return list with the splited elements

import datetime

birthdays = {}
def birthday_record():
    while True:
        name = input("Name:")
        if name == "DONE":
            break
        birthday = input("Birthday(Month-Day):")
        birthdays[name] = birthday
    print(birthdays)

birthday_record()


def d_day ():
    today = datetime.datetime.now()
    who = input("Birthday boy/girl:")
    bday_full = birthdays[who].split("-")
    bday_month = int(bday_full[0])
    bday_day = int(bday_full[1])+1
    year = today.year
    if bday_month < int(today.month):
        year += 1
    bday = datetime.datetime(year, bday_month, bday_day)
    days_left = bday-today
    if days_left < datetime.timedelta(days=1):
        print("Today is {}'s birthday!".format(who))
    else:
        print("{} days left until {}'s birthday".format(int(str(days_left).split("days")[0]),who))

d_day()