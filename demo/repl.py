import fire

class NestedGroup(object):

    def command(self):
        print('Fired NestedGroup command!')


class ParentGroup(object):
    nested = NestedGroup()

    def command(self):
        print('Grouped command')

def main():
    fire.Fire(ParentGroup)


if __name__ == '__main__':
    main()