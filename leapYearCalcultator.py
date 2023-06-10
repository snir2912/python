year = int(input("Which year do you want to check? "))

leap = year % 4 == 0

if (leap):
    print("Leap year.")
elif year % 100 == 0 and year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")