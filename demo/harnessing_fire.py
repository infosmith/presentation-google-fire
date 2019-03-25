import fire
from translate import Translator

LANGUAGES = ('en', 'es')

debug_arguments = lambda obj: obj


def demonstrate_parameters(*args, **kwargs):
    if args:
        print('args:', debug_arguments(args))
    if kwargs:
        print('kwargs: ', debug_arguments(kwargs), '\n')


def greet(name, language='en', salute='Hello', supported_languages=LANGUAGES):
    """Greet persons in their native language."""
    if language in supported_languages:
        return Translator(language).translate('{} {}!'.format(salute, name))
    else:
        return '{} {}'.format(salute, name)


parameters = demonstrate_parameters


if __name__ == '__main__':
    fire.Fire()
