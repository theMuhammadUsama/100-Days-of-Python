''' 
1. Class:
A class is like a blueprint or template for creating objects. It defines the structure (attributes or properties) 
and behavior (methods or functions) that the objects created from the class will have.
A class itself does not hold any data but provides a definition from which objects (instances) are created.
2. Object:
An object is an instance of a class. It is a concrete representation of the class with specific values for its attributes.
You can create multiple objects from the same class, and each object will have its own state.
3. Attribute:
An attribute (also called a property or field) is a variable that is bound to an object. It stores data or state 
related to that specific object. Attributes are typically defined within a class and are used to represent the 
characteristics of an object. Every object created from a class can have its own unique set of attribute values.
4. Constructor:
A constructor is a special type of method in object-oriented programming (OOP) that is used to initialize objects 
of a class. It is called automatically when an object of a class is created and is typically used to set the 
initial state of the object by assigning values to its attributes.
In Python, the constructor is called __init__.
5. Method:
A method is a function that is defined inside a class and is used to define the behavior or actions that an object can 
perform. Methods operate on the attributes of the object or class and are used to modify or retrieve data from those attributes.
'''

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1



user1 = User('004', 'Sam')
user2 = User("005", 'Kam')

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)