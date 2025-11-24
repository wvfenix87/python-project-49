from brain_games.utils import get_random_num
from brain_games.user_interactive import ask_question, is_correct_answer, goodbye

def start_progression_game(user_name: str, count_to_win: int):
    print('What number is missing in the progression?')
    count_of_right_answers = 0
    user_is_win = True
    while count_of_right_answers < count_to_win:
        start_elem = get_random_num(1, 100)
        step = get_random_num(1, 30)
        len_progression = get_random_num(5, 15)
        hide_elem = get_random_num(0, len_progression - 1)
        progression_list = generate_progression(start_elem, step, len_progression)
        answer = ask_question(generate_question(progression_list, hide_elem))
        correct_answer = progression_list[hide_elem]
        if is_correct_answer(answer, str(correct_answer)):
            count_of_right_answers += 1
        else:
            user_is_win = False
            break
    goodbye(user_name, user_is_win)

def generate_progression(start: int, step: int, progression_len: int) -> list[int]:
    result = []
    while len(result) <= progression_len:
        num = start + step * len(result)
        result.append(num)
    return result

def generate_question(progression: list[int], hide_elem: int) -> str:
    result = ''
    for num in progression:
        if progression.index(num) == hide_elem:
            result = f'{result} ..'
        else :
            result = f'{result} {num}'
    return result
