import fire
from translate import Translator

LANGUAGES = ('en', 'es')

class MultiLinguist(object):
    """Help docs parsed from class docstring."""

    def __init__(self, speaks=LANGUAGES):
        self.supported_languages = speaks

    def _is_supported_language(self, target_language: str) -> bool:
        return target_language in self.supported_languages


class Greeter(MultiLinguist):
    """Demonstrate class use in Google's Python Fire."""

    def greet(self, name: str, greeting='Hello', language='en') -> str:
        """Greet persons in their preferred language."""
        if self._is_supported_language(language):
            return Translator(language).translate('{} {}!'.format(greeting, name))
        else:
            return '{} {}'.format(greeting, name)

    def depart(self, name:str, departing='Goodbye', language='en') -> str:
        """Farewell persons in their preferred language."""
        return self.greet(name, greeting=departing, language=language)


if __name__ == '__main__':
    fire.Fire(Greeter)
