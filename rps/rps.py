# TODO: Develop a console-based Rock Paper Scissors game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement Game Rules:
# - Scissors cut Paper 
# - Paper covers Rock
# - Rock crushes Scissors
# Include user input for selecting options and display game results
# Game rules should be used to dynamically assign result strings

import random

# Define global variables
# Define list of game options
game_options = ["rock", "paper", "scissors"]

# Define dictionary of game rules
game_rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Define dictionary of game results
game_results = {
    "win": {
        "rock": "Rock crushes Scissors",
        "paper": "Paper covers Rock",
        "scissors": "Scissors cut Paper"
    },
    "lose": {
        "rock": "Rock is covered by Paper",
        "paper": "Paper is cut by Scissors",
        "scissors": "Scissors are crushed by Rock"
    },
    "draw": "It's a draw! Try again!"
}

# Define function to get user input
def get_user_input():
    user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
    if user_input in game_options:
        return user_input
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")
        return get_user_input()
    
# Define function to get computer input
def get_computer_input():
    return random.choice(game_options)

# Define function to compare user and computer inputs
def compare_inputs(user_input, computer_input):
    if user_input == computer_input:
        return "draw"
    elif game_rules[user_input] == computer_input:
        return "win"
    else:
        return "lose"
    
# Define function to display game results
def display_results(result, user_input, computer_input):
    if result == "draw":
        print(game_results[result])
    else:
        print(f"You {result}! {game_results[result][user_input]}")
    print(f"Computer chose {computer_input}.")

# Define main function
def main():
    user_input = get_user_input()
    computer_input = get_computer_input()
    result = compare_inputs(user_input, computer_input)
    display_results(result, user_input, computer_input)

# Call main function
main()