rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
Actions = [rock , paper , scissors]
print("***let's play rock,paper,scissor***")
count = 0
lives = 1
while lives <=3:
    
    lives += 1
    player_choice = int(input("choose 0-rock , 1-paper , 2-scissor :" ))
    print("Your choice!!")
    if(player_choice >= 0 and player_choice <=2):
        print(Actions[player_choice])
        computer_choice = random.randint(0,2)
        print("Computer choice!!")
        print(Actions[computer_choice])

        if player_choice == 0 and computer_choice == 2 :
            print("You Win!!")
            count+=1
        elif player_choice == 2 and computer_choice == 1 : 
            print("You Win!!")
            count+=1
        elif player_choice == 1 and computer_choice == 0 : 
            print("You Win!!")
            count+=1
        elif player_choice == computer_choice :
            print("Its A Draw!!")
        else:
            print("You Lose!!")
    else:
        print("OOps,Wrong Choice....!!")
else:
    if count >= 2 :
        print("overall : You Won!!")
    else:
        print("overall : You Lose!!")
