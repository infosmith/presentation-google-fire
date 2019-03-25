import fire
from translate import Translator


LANGUAGES = ('en', 'es')

english = 'Hello IndyPy!'
hindi = Translator('hi').translate
chinese = Translator('zh').translate
spanish = Translator('es').translate


class Greeter(object):
    """Demonstrate class use in Google's Python Fire."""

    def __init__(self, supported_languages=LANGUAGES):
        self.supported_languages = supported_languages

    def greet(self, name, salute='Hello', language='en'):
        """Greet persons in their native language."""
        if language in self.supported_languages:
            return Translator(language).translate('{} {}!'.format(salute, name))
        else:
            return '{} {}'.format(salute, name)

    def depart(self, name, salute='Goodbye', language='en'):
        """Farewell persons in their native language."""
        return self.greet(name, salute=salute, language=language)


if __name__ == '__main__':
    fire.Fire({
        'english': english,
        'hindi': hindi,
        'chinese': chinese,
        'spanish': spanish,
        'greeter': Greeter(),
    })
