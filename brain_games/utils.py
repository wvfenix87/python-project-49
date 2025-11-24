import random

def is_even_num(num: int) -> bool:
    return num % 2 == 0

def get_random_num(start=0, limit=100) -> int:
    return random.randint(start, limit)

def is_prime_num(num: int) -> bool:
    is_prime = True
    divider = 2
    while divider < num:
        if num % divider == 0:
            is_prime = False
            break
        else:
            divider=+1
    return is_prime
    