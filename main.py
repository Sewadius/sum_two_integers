#!/usr/bin/python3
import my_func as my_f

result_list = []        # Result list for multiply input


def print_intro() -> None:
    """Prints information for user"""
    print(my_f.INTRO, end='')


def print_list() -> None:
    """Prints all values in the list"""
    for i, el in enumerate(result_list, start=1):
        if el[1] < 0:
            print(f'{i}.) {el[0]} - {abs(el[1])} = {el[2]}')
        else:
            print(f'{i}.) {el[0]} + {el[1]} = {el[2]}')


def single_input() -> None:
    """Single input"""
    num_1, num_2 = my_f.get_number('first'), my_f.get_number('second')
    my_f.print_result(num_1, num_2)


def multiply_input() -> None:
    """Multiply input"""
    while True:
        try:
            print('Enter two numbers separated by a space or "q" for quit: ', end='')
            prompt = input().split()
            if len(prompt) == 1 and prompt[0].lower() == 'q':
                print(f'\nResult for {len(result_list)} calculations: ')
                print_list()
                break
            elif len(prompt) == 2:
                num1, num2 = map(int, prompt)
                result_list.append([num1, num2, num1 + num2])
            else:
                raise ValueError
        except ValueError:
            print(my_f.WRONG_NUMBERS)


def main() -> None:
    """Main function"""
    print_intro()
    while True:
        prompt = input()
        if prompt == '1':
            single_input()
            break
        elif prompt == '2':
            multiply_input()
            break
        print(my_f.WRONG_INPUT, end='')


if __name__ == '__main__':
    main()
