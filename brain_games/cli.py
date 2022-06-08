"""Command line funcionality."""
import prompt

HELLO_MSG = 'Welcome to the Brain Games!'


def welcome_user() -> str:
    """Welcomes user and asks his name.

    Returns:
        str: player's name
    """
    print(HELLO_MSG)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
