#Rules
#Rock wins against Scissors
#Paper wins against Rock
#Scissors wins against Paper

# Rock
import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choices = [rock, paper, scissor]

user_choice = int(input("What do you choice. 0 for Rock 1 for Paper and 2 for Scissors: "))
print(choices[user_choice])

computer_choice = random.randint(0,2)
print(choices[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 0 and computer_choice == 1:
    print("Computer Win!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 1 and computer_choice == 2:
    print("Computer win!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer Win!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
else:
    print("Draw")
