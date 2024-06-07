import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while not guessed:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            
if __name__ == "__main__":
    guess_the_number()