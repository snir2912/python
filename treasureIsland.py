print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

if choice1 == "left":
     choice2 = input("yout have come to lake. there is an island in the middle of the island. Type 'wait' to wait for a boat. type 'swim' to swim across the island\n").lower()
     if choice2 == "wait":
          choice3 = input("You arrive at the island! there is a house with 3 doores. red, yellow and blue. witch color do you choose?\n").lower()
          if choice3 == "red":
               print("this room full of fire, GAME OVER!")
          elif choice3 == "yellow":
               print("YOU WIN! you found the treasure")
          elif choice3 == "blue":
               print("this room full of snakes, GAME OVER!")
          else:
               print("GAME OVER!")
     else:
          print("GAME OVER. You attacked by crocodiles")
else:
     print("GAME OVER!")