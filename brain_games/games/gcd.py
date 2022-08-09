"""Command line funcionality."""
import random
import math

from brain_games.games import base_game as bg

WELCOME = 'Find the greatest common divisor of given numbers.'

MIN = 0
MAX = 20


def generate_question():
    number1 = random.randint(MIN, MAX)
    number2 = random.randint(MIN, MAX)
    answer = str(math.gcd(number1, number2))
    question = ' '.join(map(str, (number1, number2)))
    return {
        'task': question,
        'answer': answer,
    }


def start_game() -> None:
    """Starts even game in cli.
    """
    bg.start_game(WELCOME, generate_question)
