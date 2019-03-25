import fire

command_one = lambda: print('Routed to command_one variable!')

def command_two():
    print('Routed to command_two function!')

class CommandGroup(object):
    """Grouped commands."""
    def command_one(self):
        print('Routed to CommandGroup command_one method!')

def main():
    fire.Fire({
        'command_one': command_one,
        'command_two': command_two,
        'command_three': CommandGroup().command_one,
        'group': CommandGroup})

if __name__ == '__main__':
    main()