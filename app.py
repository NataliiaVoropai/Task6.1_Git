import argparse


def calculate(args) -> float:
    if args.operation == 'add':
        return args.num1 + args.num2
    elif args.operation == 'sub':
        return args.num1 - args.num2
    elif args.operation == 'mult':
        return args.num1 * args.num2
    elif args.operation == 'div':
        return args.num1 / args.num2
    else:
        return 'Unsupported operation'


def main():
    parser = argparse.ArgumentParser(description="Calculator: addition,"
                                     "substraction, division, and"
                                     "multiplication")
    parser.add_argument("operation", choices=['add', 'sub', 'mult', 'div'],
                        help='operation(add, substract, multiply, divide)')
    parser.add_argument("num1", type=float, help="The first number")
    parser.add_argument("num2", type=float, help="The second number")
    args = parser.parse_args()

    result = calculate(args)
    print(f"The result is: {result}")



