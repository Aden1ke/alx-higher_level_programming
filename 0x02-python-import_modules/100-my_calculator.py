#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    length = len(argv) - 1
    if length != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    first = int(argv[1])
    second = int(argv[3])
    operators = {'+', '-', '*', '/'}
    if argv[2] not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    if argv[2] == '+':
        print('{:} + {:d} = {:d}'.format(first, second, add(first, second)))
    elif argv[2] == '-':
        print('{:} - {:d} = {:d}'.format(first, second, sub(first, second)))
    elif argv[2] == "*":
        print('{:} * {:d} = {:d}'.format(first, second, mul(first, second)))
    elif argv[2] == '/':
        print('{:} / {:d} = {:d}'.format(first, second, div(first, second)))
