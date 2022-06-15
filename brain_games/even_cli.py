"""Command line funcionality."""
import random

from brain_games import cli


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


def generate_question():
    return str(random.randint(EVEN_MIN, EVEN_MAX))


def get_correct_answer(input_data: str) -> str:
    number = int(input_data)
    answers = {True: 'yes', False: 'no'}
    return answers[is_even(number)]


def even_game(corrects_to_win: int) -> None:
    """Starts even game in cli.

    Args:
        corrects_to_win (int): correct answers to win
    """
    name = cli.welcome_user(WELCOME)
    wins = 0
    question = generate_question()
    while cli.ask_question(question, get_correct_answer(question), name):
        wins += 1
        question = generate_question()
        if wins == corrects_to_win:
            cli.congrats(name)
            break
