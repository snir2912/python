height = float(input("please insert your height in meter units: \n"))
weight = int(input("please insert your weight in kg units: \n"))
bmi = round(weight / height ** 2)

if bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.") 
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")