"""Command line funcionality."""
import random

from brain_games import cli


WELCOME = 'What is the result of the expression?'

MIN = 0
MAX = 20


def generate_question():
    actions = ['+', '-', '*']
    arg1 = str(random.randint(MIN, MAX))
    arg2 = str(random.randint(MIN, MAX))
    action = random.choice(actions)
    return ' '.join((arg1, action, arg2))


def get_correct_answer(input_data: str) -> str:
    return str(eval(input_data))


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
