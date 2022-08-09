"""Command line funcionality."""
import random

from brain_games.games import base_game as bg

WELCOME = 'What is the result of the expression?'

MIN = 0
MAX = 20


def generate_question():
    actions = ['+', '-', '*']
    arg1 = str(random.randint(MIN, MAX))
    arg2 = str(random.randint(MIN, MAX))
    action = random.choice(actions)
    question = ' '.join((arg1, action, arg2))
    answer = str(eval(question))
    return {
        'task': question,
        'answer': answer,
    }


def start_game() -> None:
    """Starts calc game in cli.
    """
    bg.start_game(WELCOME, generate_question)
