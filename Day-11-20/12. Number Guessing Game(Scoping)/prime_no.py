
def is_prime(number):
    if number == 2:
        return True
    if number == 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

print(is_prime(5))


