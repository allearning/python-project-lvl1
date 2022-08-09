"""Command line funcionality."""
import random

from brain_games.games import base_game as bg

WELCOME = 'Answer "yes" if given number is prime. Otherwise answer "no".'

PROGRESSION_LENGHT = 10
HIDDEN_SIGN = '..'

MIN = 0
MAX = 50


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def generate_question():
    number = random.randint(MIN, MAX)
    answers = {True: "yes", False: "no"}
    answer = answers[is_prime(number)]
    return {
        'task': str(number),
        'answer': answer,
    }


def start_game() -> None:
    """Starts prime game in cli.
    """
    bg.start_game(WELCOME, generate_question)
