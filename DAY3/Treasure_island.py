print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
way = input('''you're at  a cross road , you go "Left" or "Right" ? ''').lower()
if way == "left":
    At_river = input('''You are at river "Swim" or "Wait" for boat ?''').lower()
    if At_river== "wait":
        At_finaldoor = input("Your Boat Crossed River Safely ,You are at finaldoor!!! \nChoose Which Door To Enter (Red , Yellow , Green) ? :").lower()
        if At_finaldoor == "red":
            print("You Entered A Wrong Room , You're Fired :< \n**GameOver!!** ")
        if At_finaldoor == "yellow":
            print('''Hurayy!!! You've Found Way To Treasure You Won!!! \n***Winner***''')
        if At_finaldoor == "green":
            print("You Entered A Wrong Room , You Bit By Poisonous Snakes ~~~>:- \n**GameOver!!** ")

    else:
        print("- You Attacked By An Angry Trout - \n**GameOver!!** ")


else:
    print("- You Fell in Hole - \n**GameOver!!** ")