import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }
def Calculator():
    print(art.logo)
    going = True
    f_number = float(input('Enter first number: '))


    while going:
        for key in dictionary:
            print(key)
        symbol = input('Which Operation to perform: ')
        last_number = float(input('Enter Second number: '))
        result = dictionary[symbol](f_number, last_number)
        print(f"{f_number} {symbol} {last_number} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start from new: ")
        if choice == 'y':
            f_number = result
        else:
            going = False
            print('\n'*20)
            Calculator()
            


print(Calculator())
