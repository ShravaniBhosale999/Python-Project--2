import random  # Import the random module for the computer's choice

# Define the possible choices

choices = ["rock", "paper", "scissors"]  
while True: 
    # Infinite loop to keep the game running 

    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    # Ask the user for their choice and convert it to lowercase to avoid case mismatches
    
    if user_choice == "quit": 
        print("Thanks for playing!")
        break
        # Break the loop if the user wants to stop
    if user_choice not in choices:  
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(choices)
    # Randomly select a choice for the computer
    print(f"Computer chose: {computer_choice}") 
    # Display the computer's choice

    # Compare the user and computer choices to determine the winner
    if user_choice == computer_choice:
        print("It's a tie!") 
         # Same choice means it's a tie
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!") 
        # User wins based on the rules
    else:
        print("You lose!") 
         # Otherwise, the computer wins
