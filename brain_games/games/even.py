"""Command line funcionality."""
import random

from brain_games.games import base_game as bg

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
    number = random.randint(EVEN_MIN, EVEN_MAX)
    answers = {True: "yes", False: "no"}
    answer = answers[is_even(number)]
    return {
        'task': str(number),
        'answer': answer,
    }


def start_game() -> None:
    """Starts even game in cli.
    """
    bg.start_game(WELCOME, generate_question)
