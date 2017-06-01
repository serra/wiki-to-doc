from wikidoc import __version__
import click


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__, '-V', '--version')
def cli():
    """
    wikidoc - Generate documentation from Github wikis.
    """


if __name__ == '__main__':
    cli()
