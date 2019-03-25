import fire


class NestedGroup(object):

    def command(self, arg):
        print('NestedGroup received: {}'.format(arg))


class ParentGroup(object):

    nested = NestedGroup()

    def command(self, arg):
        print('ParentGroup received: {}'.format(arg))


def main():
    fire.Fire(ParentGroup)


if __name__ == '__main__':
    main()
