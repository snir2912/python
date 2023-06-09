print("welcome to tip calcultaor")
bill = float(input("what is the total bill?\n"))
people = float(input("how many people split the bill?\n"))
precentage_tip = float(input("what precentage tip you would like to give? 10, 12 or 15\n"))
tip = (bill)  * (precentage_tip) / 100 / (people)

print("the tip is: ", tip, "NIS")