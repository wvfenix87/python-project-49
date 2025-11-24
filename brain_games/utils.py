import random

def is_even_num(num: int) -> bool:
    return num % 2 == 0

def get_random_num(limit=100) -> int:
    return random.randint(0, limit)