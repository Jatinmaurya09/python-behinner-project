import random

options = ["rock", "paper", "scissors"]

user_input = input("Enter rock, paper, or scissors: ")
computer_pick = random.choice(options)

print("Computer chose:", computer_pick)

if user_input == computer_pick:
    print("Tie")
elif(user_input == "rock" and computer_pick == "scissors") or \
     (user_input == "paper" and computer_pick == "rock") or \
     (user_input == "scissors" and computer_pick == "paper"):
    print("You win")
else:
    print("You lose")