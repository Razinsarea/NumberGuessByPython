import random
#The randrange() method returns a randomly selected element from the specified range.
num_to_guess=random.randrange(1,100)
guessed=False
attempt=0
print('Welcome to Number Guessing Game')
print('I have selected a number between 1 and 100.Can you guess?')

while not guessed:
    user_guess=(input('Enter your guess'))
    if user_guess.isdigit():
        user_guess = int(user_guess)
        attempt += 1
        if user_guess > num_to_guess:
            print('High,try again')
        elif user_guess < num_to_guess:
            print('Low,try again')
        else:
            guessed=True
            print(f'Congratutions,guessed the correct number {num_to_guess} in {attempt} attempts')
    else:
        print("Invalid input")


















