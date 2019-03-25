import fire

from translate import Translator

LANGUAGES = ('en', 'es')


class MultiLinguist(object):

    def __init__(self, greeting='Hello', departing='Goodbye', supports=LANGUAGES, target='en'):
        self.target_language = target
        self.greets_with = greeting
        self.departs_with = departing
        self.supported_languages = supports

    def _is_supported_language(self, target_language):
        return target_language in self.supported_languages

    def _translate(self, salutation):
        if self._is_supported_language(self.target_language):
            return Translator(self.target_language).translate(salutation)
        else:
            return salutation


class Greeter(MultiLinguist):
    """Demonstrate class method chaining in Google's Python Fire."""

    def greet(self, name):
        """Greet persons in their native language."""
        print(self._translate('{} {}'.format(self.greets_with, name)))
        return self

    def depart(self, name):
        """Farewell persons in their native language."""
        print(self._translate('{} {}'.format(self.departs_with, name)))
        return self

    def run(self):
        """Stop Fire from print displaying self returned from chained methods."""
        pass


if __name__ == '__main__':
    fire.Fire(Greeter)
