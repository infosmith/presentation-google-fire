"""Minimal Hello World Example with Fire."""
import fire


def greet(name):
    """Greet named entity."""
    return 'Hello {}!'.format(name)


def depart(name):
    """Farewell named entity."""
    return 'Hello {}!'.format(name)



if __name__ == '__main__':
    fire.Fire()
