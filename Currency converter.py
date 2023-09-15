# 8th Project - Currency converter
# Description: Convert currency from KRW to USD, EUR, and JPY
# Currency based on Sep 15, 4:57 AM UTC

won = []
dollar = []
euro = []
yen =[]

while True:
    krw = input("South Korean Won:")
    if krw == "DONE":
        break
    won.append(int(krw))

for i in range(len(won)):
    dollar.append(round(won[i] * 0.00075,4))
    euro.append(round(won[i] * 0.00071, 4))
    yen.append(round(won[i] * 0.11, 4))

print("South Korean Won:" + str(won))
print("United States Dollar:" + str(dollar))
print("Euro:" + str(euro))
print("Japanese Yen:" + str(yen))