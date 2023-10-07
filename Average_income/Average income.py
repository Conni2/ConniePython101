# 17th Project: Average income
# Purpose: To practice reading files and process it with split/strip
# TIL: open file -> open('file/data', 'r') as f:

with open('Average_income/October_profit.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    for line in f:
        data = line.strip().split(': ')