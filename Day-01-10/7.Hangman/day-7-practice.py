import random
from hangman_art import stages, logo3
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)
print(logo3)

placeholder = ""
chosen_length = len(chosen_word)
for letter in range(chosen_length):
    placeholder += "_ "
print(placeholder)

lives = 6
game_over = False 
correct_letter =[]
while not game_over:
    print(f"***************{lives}/6 LIVES LEFT***************")
    guess = input("Choose a letter: ").lower()
    display = ""
    if guess in correct_letter:
        print(f"You've already guessed {guess}")
    for letter in chosen_word:
        if guess == letter:
            display += guess
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_ "
    if guess not in chosen_word:
        lives -=1
        print(f"You've guessed {guess}, which is not in the word. You've lost a life")
        if lives == 0:
            game_over = True
            print(f"***************IT WAS {chosen_word}! YOU LOOSE")
    print(display)
    if "_" not in display:
        game_over = True
        print("***************YOU WIN***************")
    print(stages[lives])


