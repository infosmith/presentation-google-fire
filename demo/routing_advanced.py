import fire

class WhyFireExample(object):

    def command(self):
        print("Fired NestedGroup's command method!")

class NestedGroup(object):

    def __init__(self, nested_arg, nested_kwarg=None):
        print('NestedGroup received: ({}, {})'.format(nested_arg, nested_kwarg))

    def command(self, command_arg, command_kwarg):
        print('Nested command received: ({}, {})'.format(command_arg, command_kwarg))


class ParentGroup(object):
    nested = WhyFireExample()
    nested_group = NestedGroup

    def handler(self, handler_arg, nested_arg, handler_kwarg=None, nested_kwarg=None):
        print('Hander received: ({}, {})'.format(handler_arg, handler_kwarg))
        return self.nested_group(nested_arg, nested_kwarg)


    def command(self):
        print("Fired ParentGroup's command method!")


def main():
    fire.Fire(ParentGroup)


if __name__ == '__main__':
    main()
