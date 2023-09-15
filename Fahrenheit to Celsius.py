fahrenheit = []
celcius = []

while True:
    temp = input("Temperature(°F, Enter DONE When you are finished):")
    if temp == "DONE":
        break
    fahrenheit.append(temp)

print("Fahrenheit:"+str(fahrenheit))

for i in range(len(fahrenheit)):
    cel = round((float(fahrenheit[i])-32) * 5 / 9, 2)
    celcius.append(cel)

print("Celcius:"+str(celcius))