import fire


class Transformation(object):
    pass


class Cleaner(Transformation):

    def remove_stopwords(self, source, columns):
        return 'Removed stopwords from {} on columns: {}'.format(source, columns)


class Aggregator(Transformation):

    def group_by(self, func, source, by_field, ):
        return 'Grouped {} by {} using {}'.format(source, by_field, func)


class ExtractionManager(object):

    def download(self, uri, destination):
        print('Extracting dataset from: {}'.format(uri))
        print('Saving dataset to: {}'.format(destination))
        return 'Downloaded file from {} to {}'.format(uri, destination)


class TransformationManager(object):
    clean = Cleaner()
    aggregate = Aggregator()


class CommandGroup(object):

    def __init__(self):
        self.extract = ExtractionManager()
        self.transform = TransformationManager()


if __name__ == '__main__':
    fire.Fire(CommandGroup)
