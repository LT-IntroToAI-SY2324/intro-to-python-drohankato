# We will write a rock paper scissors game in class - Complete it in this file
import random

player_choice = "rock"
computer_choice = "Paper"

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = input("Enter a choice (rock, paper, scissors):")
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer": computer_choice}

    return choices

def check_winner(player,computer):
    print(f"You choose {player}, computer chose {computer}")
    if player == computer : 
        return "It's a tie" 
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors. You win!"
        else
            return "paper covers rock. You lose."
    elif player == "paper":
        if computer == "scissors":
            return "scissors cut paper. You lose."
        else
            return "paper "
    
choices = get _choices()
print(choices)
result = check_winner(choices[player], "rock")

print(choices)
