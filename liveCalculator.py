age = input("What is your current age? ")

years_reamining = 90 - int(age)
days = int(years_reamining) * 365
weeks = int(years_reamining) * 52
months = int(years_reamining) * 12 
years_reamining = 90 - int(age)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")