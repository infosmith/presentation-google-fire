import fire

class NestedGroup(object):

    def __init__(self, ngi_arg, ngi_kwarg=None):
        print('NGInit: ({}, {})'.format(ngi_arg, ngi_kwarg))

    def command(self, ngc_arg, ngc_kwarg):
        print('NGCommand ({}, {})'.format(ngc_arg, ngc_kwarg))


class ParentGroup(object):
    nested_group = NestedGroup

    def pipe(self, pgp_arg, ngi_arg, pgp_kwarg=None, ngi_kwarg=None):
        print('PGPipe: ({}, {})'.format(pgp_arg, pgp_kwarg))

        self.command(pgp_arg, )
        return self.nested_group(ngi_arg, ngi_kwarg)

    def chain(self, handler_arg, nested_arg, handler_kwarg=None, nested_kwarg=None):
        print('Handler received: ({}, {})'.format(handler_arg, handler_kwarg))
        return self.nested_group(nested_arg, nested_kwarg)

    def command(self, pgc_arg, pgc_kwarg):
        print('PGC received: ({}, {})'.format(pgc_arg, pgc_kwarg))

def main():
    fire.Fire(ParentGroup)


if __name__ == '__main__':
    main()