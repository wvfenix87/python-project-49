import random, prompt

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_of_right_answers = 0
    final_mesage = f'Congratulations, {name}!'
    while count_of_right_answers < 3:
        num, answer = ask_question()
        is_even = num % 2 == 0
        if answer_is_correct(is_even, answer) :
            count_of_right_answers += 1
            print('Correct!')
        else :
            print(generate_fail_mesage(is_even, answer))
            final_mesage =f"Let's try again, {name}!"
            break
    print(final_mesage)

if __name__ == "__main__":
    main()

def ask_question() -> tuple[int, str]:
    random_number = random.randint(1, 100)
    print(f'Question: {random_number}')
    answer = prompt.string(f'Your answer: ')
    return random_number, answer

def answer_is_correct(is_even: bool, answer: str) -> bool:
    if is_even and answer == 'yes':
        return True
    if not is_even and answer == 'no':
        return True
    return False

def generate_fail_mesage(is_even: bool, answer: str) -> str:
    corret_answer = 'yes'
    if not is_even:
        corret_answer = 'no'
    return f"'{answer}' is wrong answer ;(. Correct answer was '{corret_answer}'."