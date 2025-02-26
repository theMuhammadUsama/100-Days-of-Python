import random
print('Welcome to Number Guessing Game!')
print('I am guessing of a number between 0 to 100.')

mode = input('Choose a Difficulty. Type "easy" or "hard": ')
tries = 10
if mode == 'hard':
    tries = 5
print(f'You have {tries} remaining to guess the number.')
# print(tries)
looping = True

def easy_func():
    while looping:
        guess = int(input('Make a guess: '))
        if guess == random_number:
            print(f'You got it right. True answer was {guess}')
            looping == False
        elif guess < random_number:
            return 'Too low!'
        elif guess > random_number:
            return 'Too high'
        


random_number = random.randint(1, 100)
print(random_number)
easy_func()

    
