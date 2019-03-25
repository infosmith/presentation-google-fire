from pprint import pprint as pp
import fire

some_variable = 1

def some_function():
    return 'Hello function!'

class SomeClass(object):
    pass

# pp(globals())

def main():
    fire.Fire()

if __name__ == '__main__':
    main()