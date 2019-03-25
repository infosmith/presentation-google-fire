from scripted import Script

script = Script()

@script.add_controller
@script.option('-a', '--option-a', dest='option_a', help="controller option-a help text")
@script.option('-b', '--option-b', dest='option_b', help="controller option-b help text")
class CommandController(script.Controller):
    """Main parser's help menu created from Controller class docstring."""

    @script.argument('-c', '--option-c', dest='option_c', help='command_one option-c help text')
    @script.argument('arg2', dest='arg2', help='command_one arg2 help text')
    @script.argument('arg1', dest='arg1', help='command_one arg1 help text')
    def command_one(self):
        """Subparser help and desc created from command_one docstring."""
        self.fn.print(f"Called {self.fn.scope} with {self.args}")

    def helper(self):
        """Undecorated methods are not inspected."""
        self.fn.print('Helper method')

if __name__ == '__main__':
    script.execute()