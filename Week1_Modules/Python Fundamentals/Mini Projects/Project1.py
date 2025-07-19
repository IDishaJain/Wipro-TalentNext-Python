distance = int(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest Bicycle for your destination.")
elif distance < 300:
    print("I suggest Motor-Cycle for your destination.")
else:
    print("I suggest Super-Car for your destination.")
