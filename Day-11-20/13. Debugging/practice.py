from random import randint
def my_func():
    for i in range(1, 21):
        if i==20:
            print("You got it!")
        
# my_func()
# dice = ['A', 'B', 'C', 'D', 'E', 'F']
# dice_no = randint(0, 5)
# print(dice[dice_no])

# year = int(input("What's your year of birth?\n"))
# if year > 1980 and year <= 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter a valid number")
    age = int(input("How old are you?"))

if age >= 18:
    print(f"You can drive at age {age}")