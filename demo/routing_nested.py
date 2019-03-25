import fire


class NestedGroup(object):

    def __init__(self, ng_arg, ng_kwarg=None):
        print('__init__: ({}, {})'.format(ng_arg, ng_kwarg))
        self.arg = ng_arg
        self.kwarg = ng_kwarg

    def nested_command(self, ngc_arg, ngc_kwarg=''):
        print('NGC received: ({}, {})'.format(command_arg, command_kwarg))


class ParentGroup(object):
    nested_group = NestedGroup  # Instantiated at runtime

    def __init__(self, pg_arg, pg_kwarg=None):
        self.arg = pg_arg
        self.kwarg = pg_kwarg

    def grouped(self, pgc_arg, pgc_kwarg):
        print('PGC received: ({}, {})'.format(pgc_arg, pgc_kwarg))


def main():
    fire.Fire(ParentGroup)


if __name__ == '__main__':
    main()