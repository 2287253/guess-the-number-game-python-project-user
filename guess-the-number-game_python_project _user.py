import random
import time

def guess_the_number():
    print("\n🎮 Welcome to the Guess the Number Game! 🎮")
    print("I'm thinking of a number between 1 and 100...")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            
            # Validate the guess
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
            
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts!")
                print(f"The secret number was {secret_number}!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            
            # Show remaining attempts
            if attempts < max_attempts:
                print(f"You have {max_attempts - attempts} attempts remaining.")
        
        except ValueError:
            print("Please enter a valid number!")
    
    # Game over message
    if attempts >= max_attempts:
        print(f"\nGame Over! You've used all {max_attempts} attempts.")
        print(f"The secret number was {secret_number}!")

def main():
    while True:
        guess_the_number()
        
        # Ask if the user wants to play again
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
