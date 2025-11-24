import prompt

from brain_games.utils import is_even_num, get_random_num
from brain_games.user_interactive import ask_question, is_correct_answer, goodbye

def start_even_game(user_name: str, count_to_win: int):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_of_right_answers = 0
    user_is_win = True
    while count_of_right_answers < count_to_win:
        num = get_random_num()
        answer = ask_question(str(num))
        is_even = is_even_num(num)
        correct_answer = find_correct_answer(is_even, num)
        if is_correct_answer(answer, correct_answer) :
            count_of_right_answers += 1
        else :
            user_is_win = False
            break
    goodbye(user_name, user_is_win)

def find_correct_answer(is_even: bool, num: int) -> str:
    if is_even:
        return "yes"
    else:
        return "no"