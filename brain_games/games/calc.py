from brain_games.utils import get_random_num
from brain_games.user_interactive import ask_question, is_correct_answer, goodbye

def start_calc_game(user_name: str, count_to_win: int):
    print('What is the result of the expression?')
    operations_list = ["*", "+", "-"]
    count_of_right_answers = 0
    user_is_win = True
    while count_of_right_answers < count_to_win:
        random_number1 = get_random_num()
        random_number2 = get_random_num()
        opertation = operations_list[get_random_num(2)]
        question = f"{random_number1} {opertation} {random_number2}"
        answer = ask_question(question)
        correct_answer = calculate(random_number1, random_number2, opertation)
        if is_correct_answer(answer, str(correct_answer)):
            count_of_right_answers += 1
        else :
            user_is_win = False
            break
    goodbye(user_name, user_is_win)

def calculate(num1: int, num2: int, operation: str) -> int:
    match operation:
        case "*":
            return num1 * num2
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2