import random

# random_interger = random.randint(1, 10)
# print(random_interger)

# random_number_0_to_1 = random.random()  #Used to generate random float numbers between 0 and 1
# print(random_number_0_to_1)

# random_float = random.uniform(1, 5)
# print(random_float)

# random_heads_or_tails = random.randint(0,1)
# if random_heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")

# LIST
cities_of_Sindh = ["Karachi", "Hyderabad", "Sukkur", "Sanghar"]

print(cities_of_Sindh)
print(f"I am from {cities_of_Sindh[3]} city.")

cities_of_Sindh[1] = "Larkana"
cities_of_Sindh.append("Nawabshah")
print(cities_of_Sindh)

#Who will pay bill List challenge
friends = ["Zain", "Ali", "Asif", "Iqbal"]
#option
print(friends[random.randint(0,3)])
#option 2
print(random.choice(friends))