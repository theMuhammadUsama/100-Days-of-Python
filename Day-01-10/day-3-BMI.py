weight = int(input("Enter your Weight "))
height = float(input("Enter your height "))
bmi = weight/(height**2)
if bmi < 18.5:
    print("You are underweight")
elif bmi < 25:
    print("You are normal")
else:
    print("You are overweight")
