import prompt

def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    return user_name

def ask_question(mesage: str) -> str:
    print(f'Question: {mesage}')
    answer = prompt.string(f'Your answer: ')
    return answer

def is_correct_answer(answer: str, correct_answer: str) -> bool:
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False

def goodbye(user_name: str, user_is_win: bool):
    if user_is_win:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}!")