import fire

class NestedGroupOne(object):

    def command_a(self):
        print('NestedGroupOne command_a')


class NestedGroupTwo(object):

    def command_a(self):
        print('group_two nested_group command_a')


class GroupOne(object):

    nested_group = NestedGroupOne()

    def command_a(self):
        print('GroupOne command_a')


class GroupTwo(object):

    nested_group = NestedGroupTwo()

    def command_a(self):
        print('GroupTwo command_a')



class CommandGroup(object):

    def __init__(self):
        self.group_one = GroupOne()
        self.group_two = GroupTwo()



if __name__ == '__main__':
    fire.Fire(CommandGroup)
