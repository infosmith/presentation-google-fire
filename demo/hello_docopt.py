"""
Scripting with docopt.

Usage:
    hello_docopt.py greet <greet_name>
    hello_docopt.py depart <depart_name>

Options:
    -h --help     Show this screen.

"""


def greet(name):
    return 'Hello {}!'.format(name)


def depart(name):
    return 'Goodbye {}!'.format(name)


def main(args):
    if args['greet']:
        print(greet(args['<greet_name>']))
    elif args['depart']:
        print(depart(args['<depart_name>']))
    else:
        print('Unhandled arguments: {}'.format(args))


if __name__ == '__main__':
    from docopt import docopt

    script_arguments = docopt(__doc__)
    main(script_arguments)
