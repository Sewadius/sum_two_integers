#!/usr/bin/python3
from my_func import get_number, print_result

if __name__ == '__main__':
    num_1 = get_number('первое')
    num_2 = get_number('второе')

    # Расчёт и вывод результата
    print_result(num_1, num_2)
