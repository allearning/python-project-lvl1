"""Command line funcionality."""
import random
import math

from brain_games import cli

WELCOME = 'Find the greatest common divisor of given numbers.'

MIN = 0
MAX = 20


def generate_question():
    arg1 = str(random.randint(MIN, MAX))
    arg2 = str(random.randint(MIN, MAX))
    return ' '.join((arg1, arg2))


def get_correct_answer(input_data: str) -> str:
    integers = map(int, input_data.split())
    return str(math.gcd(*integers))


def start_game(corrects_to_win: int) -> None:
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
