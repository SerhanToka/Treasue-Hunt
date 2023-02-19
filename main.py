print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

door = input("You found 2 doors at the entrance, which one will you choose? Left or Right \n").lower
if door == "left":
    pool = input("You found a pool in the backyard of ancient ruins, what will you do? Swim or Wait \n").lower
    if pool == "wait":
        surpise_doors = input("While you were waiting and thinking, a voice came from behind the walls and 3 doors appeared. One with a blue stone, another with a red             stone, and the other with a green stone. Which one will you choose? Blue, Red or Green \n").lower
        if surpise_doors == "red":
            print("You found precious treasure chest!!")
        elif surpise_doors == "blue":
            print("You are crushed to death under the feet of guard golems...")
        elif surpise_doors == "green":
            print("Your blood sucked by the bruxas.")
    else:
        print("You are ripped to shreds by piranhas...")
else:
    print("You booby-trapped and started praying that death would take you...")