print("welcome to tip calcultaor")
bill = float(input("what is the total bill?\n"))
people = float(input("how many people split the bill?\n"))
precentage = float(input("what precentage tip you would like to give? 10, 12 or 15\n"))

precentage_tip = precentage / 100
total_tip = bill  * precentage_tip
tip_per_person = total_tip / people
round_tip = round(tip_per_person, 2)

print(f"Each person should give {round_tip}NIS for tip")