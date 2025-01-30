def greet():
    print("Hello")
    print("How are you")
    print("How's the day")

greet()

#Function with a input:
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}")

greet_with_name("Usama")
# Here name is parameter and Usama is argument

#Function with more than one input:
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")

greet_with("Usama", "Karachi")
greet_with(location="Karachi", name="Usama")