#!/usr/bin/env python3
"""Even-no even game."""
import random
import prompt
from brain_games import cli


HELLO_MSG = 'Welcome to the Brain Games!'
CORRECT_STRING = 'Correct!'
ANSWER_STRING = 'Your answer: '
CONGRATS_STRING = 'Congratulations'
SUCCESS_TO_WIN = 3
WELCOME = 'Answer "yes" if the number is even, otherwise answer "no".'

EVEN_MIN = 0
EVEN_MAX = 1000


def is_even(int_: int) -> bool:
    """Check if integer is even.

    Args:
        int_ (int): integer to check

    Returns:
        bool: True if even
    """
    return int_ % 2 == 0


def congrats(name):
    print(f'{CONGRATS_STRING}, {name}!')


def ask_question(question_text: str, correct_answer: str, name: str) -> bool:
    """Asks a question and checks if answer is correct.

    Args:
        question_text (str): question to ask
        correct_answer (str): correct answer
        name (str): player name

    Returns:
        bool: True if answer is correct, False otherwise
    """
    print(f'Question: {question_text}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print(CORRECT_STRING)
        return True
    print(
        f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    )
    print(f"Let's try again, {name}!")
    return False


def generate_question():
    return str(random.randint(EVEN_MIN, EVEN_MAX))


def get_correct_answer(input_data: str) -> str:
    number = int(input_data)
    answers = {True: 'yes', False: 'no'}
    return answers[is_even(number)]


def start_game(corrects_to_win: int) -> None:
    """Starts even game in cli.

    Args:
        corrects_to_win (int): correct answers to win
    """
    name = cli.welcome_user(WELCOME)
    wins = 0
    question = generate_question()
    while ask_question(question, get_correct_answer(question), name):
        wins += 1
        question = generate_question()
        if wins == corrects_to_win:
            congrats(name)
            break


def main():
    start_game(SUCCESS_TO_WIN)


if __name__ == '__main__':
    main()
