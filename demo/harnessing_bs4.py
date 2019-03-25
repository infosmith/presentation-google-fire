import os

import bs4
import fire
import requests


class Page:

    def __init__(self, dom=None):
        self.dom = dom

    def __getitem__(self, css):
        return self.select(css)

    @staticmethod
    def from_file(path):
        with open(path, 'r') as f:
            return Page(Page.parse_dom(f.read()))

    @staticmethod
    def from_url(url):
        return Page(Page.parse_dom(requests.get(url).text))

    @staticmethod
    def parse_dom(content, parser='lxml'):
        return bs4.BeautifulSoup(content, parser)

    def select(self, css):
        return self.dom.select(css)

    def to_file(self, path):
        with open(path, 'w') as handle:
            handle.write(self.dom.prettify())


class IndyPyExample(object):
    """Download and scrape data from the web using BS4."""

    def _delegate(self, elements, member):
        for element in elements:
            if hasattr(element, member) and getattr(element, member) is not None:
                yield getattr(element, member)
            else:
                yield "{} object does not have member: {}".format(element.__class__.__name__, member)

    def _print(self, elements):
        for element in elements:
            print(element)

    def download(self, url, destination):
        """Download contents at URI and write it to file."""
        Page.from_url(url).to_file(os.path.abspath(destination))
        print('Downloaded: {}'.format(url))

    def search(self, source, selector, invoke=None):
        """Scrape data from file using CSS selectors via BS4."""
        page = Page.from_file(os.path.abspath(source))
        elements = page[selector]
        if invoke:
            self._print(self._delegate(elements, invoke))
        else:
            self._print(elements)


def main():
    fire.Fire(IndyPyExample)

if __name__ == '__main__':
    main()
    
