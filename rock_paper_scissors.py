import random  # Module to generate random choices for the AI

# Initialize scores
ai_points = 0
user_points = 0

# List of valid choices
choices = ["rock", "paper", "scissors"]

# Function to display the current score
def display_score(user_points, ai_points):
    print(f"Total score: {user_points} (player) - {ai_points} (AI)")

# Function to determine the winner of a round
def determine_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "tie"  # Return "tie" if both choices are the same
    elif (user_choice == "rock" and ai_choice == "paper") or \
         (user_choice == "paper" and ai_choice == "scissors") or \
         (user_choice == "scissors" and ai_choice == "rock"):
        return "ai"  # Return "ai" if the AI wins
    else:
        return "user"  # Return "user" if the user wins

# Function to announce the result of a round
def announce_result(user_choice, ai_choice):
    result = determine_winner(user_choice, ai_choice)
    if result == "tie":
        print("It's a tie.")  # Announce a tie
    elif result == "ai":
        print("The AI wins this round.")  # Announce AI win
    elif result == "user":
        print("You win this round.")  # Announce user win
    display_score(user_points, ai_points)  # Display the updated score

# Main game loop, runs until either the user or AI reaches 3 points
while ai_points < 3 and user_points < 3:
    user_choice = input("Rock, paper, or scissors? ").lower()  # Get user input and convert to lowercase
    
    if user_choice not in choices:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.\n")
        continue  # Skip to the next iteration if input is invalid

    print(f"You chose {user_choice}.")  # Show user's choice
    ai_choice = random.choice(choices)  # AI makes a random choice
    print(f"The AI chose {ai_choice}.")  # Show AI's choice

    winner = determine_winner(user_choice, ai_choice)  # Determine the winner of the round
    if winner == "ai":
        ai_points += 1  # Increment AI's score
    elif winner == "user":
        user_points += 1  # Increment user's score

    announce_result(user_choice, ai_choice)  # Announce the result of the round

# Announce the final winner based on scores
if ai_points == 3:
    print(f"The AI wins the game!\nFinal score: {user_points} (player) - {ai_points} (AI)")
else:
    print(f"Congratulations! You win the game!\nFinal score: {user_points} (player) - {ai_points} (AI)")
