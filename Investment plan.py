# 5th Project - Investment plan
# Description: Compare two different investment types (simple interest/compound interest) with different interest rates | Purpose: To practice while & if statment
# The difference of interest between two plans are only displayed upto 4 decimal places
# TIL: How to calculate the compound rate (need to change the condition in the while statement)

#Receiving values
capital = int(input("Initial capital:"))
startingyear = int(input("Starting year:"))
endingyear = int(input("Desired end year:"))
interestrate_simple = float(input("Interest rate for simple interest:")) / 100
interestrate_compound = float(input("Interest rate for compound interest:")) / 100

#Variables
simple = capital * (1+(endingyear-startingyear)*interestrate_simple)
compound = capital
year = startingyear

while year < endingyear:
    compound = compound * (1+interestrate_compound)
    year += 1

comparison = round(simple - compound, 4)
if comparison < 0:
    comparison = abs(comparison)
    print("Compound interest is more profitable than simple interest by ${}.".format(comparison))
elif comparison == 0:
    print("Interests from two plans are same")
else:
    print("Simple interest is more profitable than compound interest plan by ${}.".format(comparison))