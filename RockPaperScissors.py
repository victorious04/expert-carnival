import random

possibleOptions = ["Rock","Paper","Scissors"]
userWins = 0
compWins = 0

for x in range (1,4):
    userChoice = input("Please choose Rock, Paper or Scissors.")
    compChoice = random.choice(possibleOptions)

    print(f"Computer Chose: {compChoice}")
    if (userChoice == "Rock" and compChoice == "Scissors") or (userChoice == "Paper" and compChoice == "Rock") or (userChoice == "Scissors" and compChoice == "Paper"): 
        print("You won this round!")
        userWins+=1
    else:
        print("You lost this round!")
        compWins+=1
if userWins > compWins:
    print("You Win!")
else:
    print("Better luck next time")

"""
For this program the variables are easy to read and the code is kept straightforward with comments to expalin what happens
in each section. To improve this code, I would add input validation such as prescence check or string check. 
Also to include scenarios where they draw and both players get a point since right now if there is a draw, the
computer automatically wins the round
"""