print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_names = name1+name2
lower_case_names = combine_names.lower()

t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")
true = t+r+u+e

l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")
love = l+o+v+e

score_love_str = str(true)+str(love)
score_love = int(score_love_str)

if score_love < 10 or score_love > 90:
    print(f"Your score is {score_love}, you go together like coke and mentos.")
elif score_love >= 40 and score_love < 50:
    print(f"Your score is {score_love}, you are alright together.")
else:
    print(f"Your score is {score_love}.")