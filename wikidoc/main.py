import click
from wikidoc import build_docs
from wikidoc._version import __version__


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__, '-V', '--version')
def cli():
    """
    wikidoc - Generate documentation from a Github wiki.
    """


@cli.command(name="build")
@click.option('--repo',
              default="https://github.com/serra/wiki-to-doc.wiki.git")
@click.option('--name',
              default="wiki-to-doc.wiki")
def build(repo, name):
    """
    Get the latest version of the wiki and build into an html website.
    """
    build_docs.build(repo, name)
