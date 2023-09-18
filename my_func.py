# Some constants and functions

INTRO = '''== Welcome to "Sum two integers" project! ==
Please enter "1" for single input or "2" for multiply input: '''

WRONG_INPUT = 'Wrong input! Try again: '
WRONG_NUMBERS = 'Wrong numbers! Try again!'


def counts_sum(a: int, b: int) -> int:
    """Counts sum for two integer numbers"""
    return a + b


def get_number(word: str) -> int:
    """Get numbers from user"""
    number = None
    while True:
        try:
            number = int(input(f'Enter the {word} integer: '))
            break
        except ValueError:
            print(f'You entered the wrong integer. Try again!\n')
            continue
    return number


def print_result(number_1: int, number_2: int) -> None:
    """Prints result for single input"""
    print(f'Result of sum of numbers "{number_1}" and "{number_2}": '
          f'{counts_sum(number_1, number_2)}')
