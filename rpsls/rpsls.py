# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement Game Rules:
# - Scissors decapitate Lizard
# - Scissors cut Paper 
# - Paper covers Rock
# - Paper disproves Spock
# - Rock crushes Lizard
# - Rock crushes Scissors
# - Lizard poisons Spock
# - Lizard eats Paper
# - Spock smashes Scissors
# - Spock vaporizes Rock
# Include user input for selecting options and display game results

import random

# Define global variables
# Define list of game options
game_options = ["rock", "paper", "scissors", "lizard", "spock"]

# Define dictionary of game rules
game_rules = {
    "rock": {
        "lizard": "crushes",
        "scissors": "crushes"
    },
    "paper": {
        "rock": "covers",
        "spock": "disproves"
    },
    "scissors": {
        "lizard": "decapitates",
        "paper": "cuts"
    },
    "lizard": {
        "spock": "poisons",
        "paper": "eats"
    },
    "spock": {
        "scissors": "smashes",
        "rock": "vaporizes"
    }
}

# Define dictionary of game results
game_results = {
    "win": {
        "rock": {
            "lizard": "Rock crushes Lizard",
            "scissors": "Rock crushes Scissors"
        },
        "paper": {
            "rock": "Paper covers Rock",
            "spock": "Paper disproves Spock"
        },
        "scissors": {
            "lizard": "Scissors decapitate Lizard",
            "paper": "Scissors cut Paper"
        },
        "lizard": {
            "spock": "Lizard poisons Spock",
            "paper": "Lizard eats Paper"
        },
        "spock": {
            "scissors": "Spock smashes Scissors",
            "rock": "Spock vaporizes Rock"
        }
    },
    "lose": {
        "rock": {
            "paper": "Paper covers Rock",
            "spock": "Spock vaporizes Rock"
        },
        "paper": {
            "scissors": "Scissors cut Paper",
            "lizard": "Lizard eats Paper"
        },
        "scissors": {
            "rock": "Rock crushes Scissors",
            "spock": "Spock smashes Scissors"
        },
        "lizard": {
            "rock": "Rock crushes Lizard",
            "scissors": "Scissors decapitate Lizard"
        },
        "spock": {
            "paper": "Paper disproves Spock",
            "lizard": "Lizard poisons Spock"
        }
    },
    "tie": {
        "rock": {
            "rock": "Rock equals Rock"
        },
        "paper": {
            "paper": "Paper equals Paper"
        },
        "scissors": {
            "scissors": "Scissors equals Scissors"
        },
        "lizard": {
            "lizard": "Lizard equals Lizard"
        },
        "spock": {
            "spock": "Spock equals Spock"
        }
    }
}

# Define function to get user input
def get_user_input():
    # Prompt user for input
    user_input = input("Enter your choice (Rock, Paper, Scissors, Lizard, Spock): ")
    # Convert input to lowercase
    user_input = user_input.lower()
    # Return user input
    return user_input

# Define function to get computer input
def get_computer_input():
    # Generate random number between 0 and 4
    computer_input = random.randint(0, 4)
    # Return computer input
    return computer_input

# Define function to validate user input
def validate_user_input(user_input):
    # Check if user input is in list of game options
    if user_input in game_options:
        # Return True
        return True
    # Otherwise
    else:
        # Return False
        return False
    
# Define function to validate computer input
def validate_computer_input(computer_input):
    # Check if computer input is in list of game options
    if computer_input in game_options:
        # Return True
        return True
    # Otherwise
    else:
        # Return False
        return False

# Define function to determine game results
def determine_game_results(user_input, computer_input):
    # Check if user input is equal to computer input
    if user_input == computer_input:
        # Return tie
        return "tie"
    # Otherwise
    else:
        # Check if user input is rock
        if user_input == "rock":
            # Check if computer input is lizard
            if computer_input == "lizard":
                # Return win
                return "win"
            # Otherwise
            else:
                # Return lose
                return "lose"
        # Check if user input is paper
        elif user_input == "paper":
            # Check if computer input is rock
            if computer_input == "rock":
                # Return win
                return "win"
            # Otherwise
            else:
                # Return lose
                return "lose"
        # Check if user input is scissors
        elif user_input == "scissors":
            # Check if computer input is paper
            if computer_input == "paper":
                # Return win
                return "win"
            # Otherwise
            else:
                # Return lose
                return "lose"
        # Check if user input is lizard
        elif user_input == "lizard":
            # Check if computer input is spock
            if computer_input == "spock":
                # Return win
                return "win"
            # Otherwise
            else:
                # Return lose
                return "lose"
        # Check if user input is spock
        elif user_input == "spock":
            # Check if computer input is scissors
            if computer_input == "scissors":
                # Return win
                return "win"
            # Otherwise
            else:
                # Return lose
                return "lose"
            
# Define function to display game results
def display_game_results(user_input, computer_input, game_results):
    # Check if game results is tie
    if game_results == "tie":
        # Display tie message
        print("You chose " + user_input + ". The computer chose " + computer_input + ". " + user_input.capitalize() + " equals " + computer_input.capitalize() + ".")
    # Otherwise
    else:
        # Check if game results is win
        if game_results == "win":
            # Display win message
            print("You chose " + user_input + ". The computer chose " + computer_input + ". " + game_results.capitalize() + ". " + user_input.capitalize() + " " + game_rules[user_input][computer_input] + " " + computer_input.capitalize() + ".")
        # Otherwise
        else:
            # Display lose message
            print("You chose " + user_input + ". The computer chose " + computer_input + ". " + game_results.capitalize() + ". " + computer_input.capitalize() + " " + game_rules[computer_input][user_input] + " " + user_input.capitalize() + ".")

# Define main function
def main():
    # Display welcome message
    print("Welcome to Rock Paper Scissors Lizard Spock!")
    # Get user input
    user_input = get_user_input()
    # Validate user input
    while not validate_user_input(user_input):
        # Display error message
        print("Invalid input. Please try again.")
        # Get user input
        user_input = get_user_input()
    # Get computer input
    computer_input = get_computer_input()
    # Validate computer input
    while not validate_computer_input(computer_input):
        # Get computer input
        computer_input = get_computer_input()
    # Determine game results
    game_results = determine_game_results(user_input, game_options[computer_input])
    # Display game results
    display_game_results(user_input, game_options[computer_input], game_results)
    # Display goodbye message
    print("Thanks for playing Rock Paper Scissors Lizard Spock!")

# Call main function
main()