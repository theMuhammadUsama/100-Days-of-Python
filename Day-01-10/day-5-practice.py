# fruits = ["Apple", "Mango", "Orange"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " juice")

#Numbers
student_socres = [111, 124, 140, 160, 133, 99, 150]
total_score = sum(student_socres)
print(total_score)
total =0
maximum =0
for score in student_socres:
    if maximum < score:
        maximum =score
    total += score

print(f"Maximum number in list = {maximum}")
print(max(student_socres))

print(f"Total score = {total}")

#Range
sum_of_range = 0
for number in range(1, 101):
    sum_of_range += number
print(sum_of_range)

#Fizzbuzz
numb_fizz = 0
for number in range(0, 101):
    if number % 3 ==0 and number % 5 == 0:
         print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)
