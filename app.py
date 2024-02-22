import argparse


def calculate(args) -> float:
    if args.operation == 'add':
        return args.num1 + args.num2
    elif args.operation == 'substract':
        return args.num1 - args.num2
    else:
        return 'Unsupported operation'


def main():
    parser = argparse.AtgumentParser(descritpion="Calculator: addition and substraction")
    parser.add_argument("operation", choices=['add', 'subsctract'], help='operation(add or subsctract)')
    parser.add_argument("num1", type=float, help="The first number")
    parser.add_argument("num2", type=float, help="The second number")
    args = parser.parse_args()

    result = calculate(args)
    print(f"The result is: {result}")


