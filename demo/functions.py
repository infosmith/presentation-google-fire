"""Functions example"""
import fire
from translate import Translator

LANGUAGES = ('en', 'es', 'zh', 'hi', 'ar', 'de', 'cy')
GREETING_MSG = 'Hello {}, welcome to IndyPy!'
DEPARTING_MSG = 'Goodbye {}, enjoy the conference!'

debug_arguments = lambda obj: obj


def demonstrate_parameters(*args, **kwargs):
    if args:
        print('args:', debug_arguments(args))
    if kwargs:
        print('kwargs: ', debug_arguments(kwargs), '\n')


def greet(name, language='en', greeting=GREETING_MSG, supported_languages=LANGUAGES):
    """Greet persons in their native language."""
    if language in supported_languages:
        return Translator(language).translate(greeting.format(name))
    else:
        return greeting.format(name)


if __name__ == '__main__':
    fire.Fire()
