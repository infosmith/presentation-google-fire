"""Minimal hello world example with argparse."""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('command', help='Say greeting or farewell.')
parser.add_argument('name', help='Name to salute.')


def greet(name):
    return 'Hello {}!'.format(name)

def depart(name):
    return 'Goodbye {}!'.format(name)

def main(args):
    if args.command == 'greet':
        print(greet(args.name))
    elif args.command == 'depart':
        print(depart(args.name))
    else:
        print('Unhandled arguments: {}'.format(args))


if __name__ == '__main__':
    main(parser.parse_args())
