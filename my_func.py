def counts_sum(a: int, b: int) -> int:
    return a + b


def get_number(word: str) -> int:
    number = None
    while True:
        try:
            number = int(input(f'Enter the {word} integer: '))
            break
        except ValueError:
            print(f'You entered the wrong integer!!\n')
            continue
    return number


def print_result(number_1: int, number_2: int) -> None:
    print(f'Result of sum of numbers "{number_1}" and "{number_2}": '
          f'{counts_sum(number_1, number_2)}')
