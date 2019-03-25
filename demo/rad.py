import fire
from translate import Translator

LANGUAGE = 'en'
GREETING = 'Hello {}, welcome to Automate!'
TRANSLATOR = Translator


def greet(name, msg=GREETING, lang=LANGUAGE):
    """Greet people in their preferred language."""
    return Translator(lang).translate(msg.format(name))


class Greeter(object):

    def __init__(self, translator=TRANSLATOR, native_language=LANGUAGE, greeting=GREETING):
        self.translator = translator
        self.native_language = native_language
        self.greeting = greeting

    def translate(self, text, target_language):
        if target_language:
            return self.translator(target_language).translate(text)
        else:
            return self.translator(self.native_language).translate(text)

    def greet(self, name, language=None):
        """Greet people in their preferred language."""
        return self.translate(self.greeting.format(name), language)


def main():
    fire.Fire()


if __name__ == '__main__':
    main()
