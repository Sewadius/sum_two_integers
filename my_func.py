def counts_sum(a: int, b: int) -> int:
    return a + b


def get_number(word: str) -> int:
    number = None
    while True:
        try:
            number = int(input(f'Введите {word} целое число: '))
            break
        except ValueError:
            print(f'Вы неверно ввели {word} число!\n')
            continue
    return number


def print_result(number_1: int, number_2: int) -> None:
    print(f'Результат суммы чисел {number_1} и {number_2}: '
          f'{counts_sum(number_1, number_2)}')
