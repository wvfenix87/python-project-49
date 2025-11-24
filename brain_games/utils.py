import random

def is_even_num(num: int) -> bool:
    return num % 2 == 0

def get_random_num(start=0, limit=100) -> int:
    return random.randint(start, limit)