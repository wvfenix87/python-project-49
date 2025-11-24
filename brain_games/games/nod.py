import math

from brain_games.utils import get_random_num
from brain_games.user_interactive import ask_question, is_correct_answer, goodbye

def start_nod_game(user_name: str, count_to_win: int):
    print("Find the greatest common divisor of given numbers.")
    count_of_right_answers = 0
    user_is_win = True
    while count_of_right_answers < count_to_win:
        random_number1 = get_random_num()
        random_number2 = get_random_num()
        question = f"{random_number1} {random_number2}"
        answer = ask_question(question)
        correct_answer = find_nod(random_number1, random_number2)
        if is_correct_answer(answer, str(correct_answer)):
            count_of_right_answers += 1
        else:
            user_is_win = False
            break
    goodbye(user_name, user_is_win)

def find_nod(num1: int, num2: int) -> int:
    return math.gcd(num1, num2)