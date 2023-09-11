#This is for comparint two different investment type (simple interest/compound interest) with different interest rate to make the best invetstment plan
#input values are 1) initial capital 2) investment year(From to로 받아도됨 이건 생각 좀 해보기) 3)interest rate
#currency = $

#입력값 받기
capital = int(input("Initial capital:"))
startingyear = int(input("Starting year:"))
endingyear = int(input("Desired end year:"))
interestrate_simple = float(input("Interest rate for simple interest:")) / 100
interestrate_compound = float(input("Interest rate for compound interest:")) / 100

#변수 정의
simple = capital * (1+(endingyear-startingyear)*interestrate_simple)
compound = capital
year = startingyear

while year < endingyear:
    compound = compound * (1+interestrate_compound)
    year += 1

print(simple)
print(compound)