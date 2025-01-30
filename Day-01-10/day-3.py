# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("Your entered an even number!")
# else:
#     print("You entered an odd number!")

height = int(input("Enter your height in cm: "))
bill = 0
print("Welcome to the roller coaster!")
if height >= 120:
    print("You can ride roller coaster! ")
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Child ticket costs 5$.")
        bill = 5
    elif age <= 18:
        print("Youth ticket coste 7$.")
        bill = 7
    elif age <= 55 and age >= 45:
        print("Your ticket is free. ")
        bill = 0
    else:
        print("Adult ticket costs 12$. ")
        bill = 12
    want_photo = input("Do you want photo taken. Press y for yes and n for no. ")
    if want_photo == "y":
        bill +=3
    print(f"Your final bill is ${bill}")
    
    
else:
    print("Sorry you need to grow taller")