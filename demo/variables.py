"""Variables example."""
import fire
from translate import Translator

english = 'Hello IndyPy!'
german = Translator('de').translate
arabic = lambda x: Translator('ar').translate(x)
american_english = Translator('en-us').translate

routes = {
    'american_english': american_english,
    'arabic': arabic,
    'english': english,
    'german': german,
}

routes['ar'] = routes['arabic']
routes['de'] = routes['german']
routes['en'] = routes['english']
routes['en-us'] = routes['american_english']


def main():
    fire.Fire(routes)


if __name__ == '__main__':
    main()
