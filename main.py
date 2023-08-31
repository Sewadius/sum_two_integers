#!/usr/bin/python3
from my_func import get_number, print_result

if __name__ == '__main__':
    num_1 = get_number('first')
    num_2 = get_number('second')

    # Calculation and result output
    print_result(num_1, num_2)
