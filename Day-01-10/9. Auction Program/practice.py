#Dictionary
programming_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.", 
    }
print(programming_dictionary)
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Wipe and entire dicitionay
#programming_dictionary = {}

#Edit and item in dictionary
programming_dictionary["Bug"] = "A moth in computer."
print(programming_dictionary)

#Loop through the dictionary
for thing in programming_dictionary:
    print(thing) # This will only print all the keys in dictionary
    print(programming_dictionary[thing]) #This will print the values for the key

#NESTING LISTS AND DICTIONARIES:
# Nesting a list in Dictionary and accessing items
travel_log = {
    "Sindh": ["Hyderabad", "Karachi", "Nawabshah"],
    "Punjab": ["Lahore", "Gujrat", "Faisalabad"],
}
print(travel_log['Sindh'][1])
# Nesting a List inside a list and accessing items
nested_list = ['A', 'B', ['C', 'D']]
print(nested_list[2][1])
# Nesting a Dictionary inside Dictionary and then nesting List inside that nested Dictionary then accessing items
travel_log_2 = {
    "Sindh": {
        "Cities_visited": ["Hyderabad", "Karachi", "Nawabshah"],
        "Total_visits": 5
    },
    "Punjab": {
        "Cities_visited": ["Lahore", "Gujrat", "Faisalabad"],
        "Total_visits": 1
    },
}
print(travel_log_2["Punjab"]["Cities_visited"][2])