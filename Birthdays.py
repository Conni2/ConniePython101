# 18th Project: Birthdays
# Purpose: To practice datetime module

import datetime

birthdays = {}

while True:
    name = input("Name:")
    if name == "DONE":
        break
    birthday = input("Birthday(MM-DD):")
    birthdays[name] = birthday

print(birthdays)