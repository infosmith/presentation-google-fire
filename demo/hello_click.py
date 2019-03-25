"""Minimal hello world example with Click."""
import click


@click.group()
def cli():
    """Scripting with Click."""
    pass


@cli.command()
@click.argument('name')
def greet(name):
    """Echo greeting."""
    click.echo('Hello {}!'.format(name))


@cli.command()
@click.argument('name')
def depart(name):
    """Echo farewell."""
    click.echo('Goodbye {}!'.format(name))


cli.add_command(greet)
cli.add_command(depart)

if __name__ == '__main__':
    cli()
