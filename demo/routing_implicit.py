import fire

command_one = lambda: print('Routed to command_one variable!')

def command_two():
    print('Routed to command_two function!')

class CommandGroup(object):
    """Grouped commands."""
    def command_one(self):
        print('Routed to CommandGroup command_three method!')

def main():
    fire.Fire()

if __name__ == '__main__':
    main()