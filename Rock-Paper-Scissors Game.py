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

your_choice = input("What is your choice? Rock, Paper, Scissors :")

if your_choice == "rock":
    print(f"\n You've chosen \n{rock}:")
elif your_choice == "paper":
    print(f"\n You've chosen \n{paper}:")
elif your_choice == "scissors":
    print(f"\n You've chosen \n{scissors}:")
else:
    print("You wrote wrong!")

choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(choice)

if computer_choice == "rock":
    print(f"\n The computer's chosen \n{rock}:")
elif computer_choice == "paper":
    print(f"\n The computer's chosen \n{paper}:")
elif computer_choice == "scissors":
    print(f"\n The computer's chosen \n{scissors}:")

if computer_choice == "rock":
    if your_choice == "scissors":
        print("You lose :(")
    elif your_choice == "paper":
        print("You win!")
    else:
        print("Nobody wins")

if computer_choice == "scissors":
    if your_choice == "paper":
        print("You lose :(")
    elif your_choice == "rock":
        print("You win!")
    else:
        print("Nobody wins")

if computer_choice == "paper":
    if your_choice == "scissors":
        print("You lose :(")
    elif your_choice == "rock":
        print("You win!")
    else:
        print("Nobody wins")
