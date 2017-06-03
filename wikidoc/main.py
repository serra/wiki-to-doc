import click

__version__ = '0.1.0'


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__, '-V', '--version')
def cli():
    """
    wikidoc - Generate documentation from a Github wiki.
    """
    click.echo('starting the cli ...')


@cli.command(name="build")
def build():
    click.echo('building the wiki ... ')
    click.echo('build done.')
