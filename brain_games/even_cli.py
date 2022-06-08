"""Command line funcionality."""
import random

import prompt

from brain_games import cli

HELLO_MSG = 'Welcome to the Brain Games!'
CORRECT_STRING = 'Correct!'

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


def welcome_even_game() -> str:
    """Welcomes user for even-game.

    Returns:
        str: Player's name
    """
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def ask_for_even(name) -> str:
    answers = {True: 'yes', False: 'no'}
    number = random.randint(EVEN_MIN, EVEN_MAX)
    print('Question:', str(number))
    correct_answer = answers[is_even(number)]
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print(CORRECT_STRING)
        return True
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")

    print(f"Let's try again, {name}!")
    return False


def even_game(corrects_to_win: int) -> None:
    """Starts even game in cli.

    Args:
        corrects_to_win (int): correct answers to win
    """
    name = welcome_even_game()
    wins = 0
    while ask_for_even(name):
        wins += 1
        if wins == corrects_to_win:
            print(f'Congratulations, {name}!')
            break
