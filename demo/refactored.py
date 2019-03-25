import fire
from translate import Translator

DEFAULT_LANGUAGE = 'en'
DEFAULT_GREETING = 'Hello {}, welcome to Automate!'

def greet(name, msg=DEFAULT_GREETING, lang=DEFAULT_LANGUAGE):
    """Greet people in their preferred language."""
    return Translator(lang).translate(msg.format(name))

def main():
    fire.Fire()


if __name__ == '__main__':
    main()
