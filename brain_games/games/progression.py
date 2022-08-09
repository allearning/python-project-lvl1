"""Command line funcionality."""
import random

from brain_games.games import base_game as bg

WELCOME = 'What number is missing in the progression?'

PROGRESSION_LENGHT = 10
HIDDEN_SIGN = '..'

MIN = 0
MAX = 20
MIN_STEP = 1
MAX_STEP = 20


def generate_question():
    start = random.randint(MIN, MAX)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression = list(range(
        start,
        start + step * PROGRESSION_LENGHT + 1,
        step,
    ))

    index_to_hide = random.randint(0, PROGRESSION_LENGHT - 1)
    answer = str(progression[index_to_hide])
    progression[index_to_hide] = HIDDEN_SIGN

    return {
        'task': ' '.join(map(str, progression)),
        'answer': answer,
    }


def start_game() -> None:
    """Starts progression game in cli.
    """
    bg.start_game(WELCOME, generate_question)
