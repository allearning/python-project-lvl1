"""Command line funcionality."""
import prompt

HELLO_MSG = 'Welcome to the Brain Games!'
CORRECT_STRING = 'Correct!'
ANSWER_STRING = 'Your answer: '
CONGRATS_STRING = 'Congratulations'


def welcome_user(optional_part: str or None) -> str:
    """Welcomes user and asks his name.

    Args:
       optional_part (strorNone): additional welcome-string

    Returns:
        str: player's name
    """
    print(HELLO_MSG)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    if optional_part is not None:
        print(optional_part)
    return name
