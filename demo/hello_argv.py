"""Minimal hello world example with sys.argv."""
import sys


def greet(name):
    return 'Hello {}!'.format(name)


def depart(name):
    return 'Goodbye {}!'.format(name)


def is_valid_arguments(arguments):
    return (2 < len(arguments) < 4) and arguments[1] in ['greet', 'depart']


def main(args):
    if not is_valid_arguments(args):
        print('Unhandled arguments: {}'.format(sys.argv))
    elif args[1] == 'greet':
        print(greet(sys.argv[2]))
    elif args[1] == 'depart':
        print(depart(sys.argv[2]))


if __name__ == '__main__':
    main(sys.argv)
