"""Command line funcionality."""
import prompt

HELLO_MSG = 'Welcome to the Brain Games!'
CORRECT_STRING = 'Correct!'
ANSWER_STRING = 'Your answer: '
CONGRATS_STRING = 'Congratulations'
SUCCESS_TO_WIN = 3


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


def ask_question(question_text: str, correct_answer: str, name: str) -> bool:
    """Asks a question and checks if answer is correct.

    Args:
        question_text (str): question to ask
        correct_answer (str): correct answer
        name (str): player name

    Returns:
        bool: True if answer is correct, False otherwise
    """
    print(f'Question: {question_text}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print(CORRECT_STRING)
        return True
    print(
        f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    )
    print(f"Let's try again, {name}!")
    return False


def congrats(name):
    print(f'{CONGRATS_STRING}, {name}!')


def start_game(welcome_message, generate_question) -> None:
    """Starts game in cli.

    Args:
        welcome_message: message to welcome user
        generate_question: function, generating {'task'="...", 'answer' = "..."}
    """

    name = welcome_user(welcome_message)
    wins = 0
    question = generate_question()
    while ask_question(question['task'], question['answer'], name):
        wins += 1
        question = generate_question()
        if wins == SUCCESS_TO_WIN:
            congrats(name)
            break
