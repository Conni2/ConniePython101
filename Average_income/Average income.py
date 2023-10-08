# 17th Project: Average income
# Purpose: To practice reading files and process it with split/strip
# TIL: open file -> open('file/data', 'r') as f:

with open('Average_income/October_profit.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    for line in f:
        data = line.strip().split(': ')
        total_revenue += int(data[1])
        total_days += 1
    avg_revenue = round(total_revenue/total_days, 2)
    print("Total revenue of {} days: {}".format(total_days, total_revenue))
    print("Average avenue per day: {}".format(avg_revenue))