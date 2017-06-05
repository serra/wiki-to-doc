from setuptools import setup
from setuptools import find_packages

__version__ = '0.2.1'

setup(
    name='wikidoc',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'mkdocs',
        'GitPython',
    ],
    entry_points='''
        [console_scripts]
        wikidoc=wikidoc.main:cli
    ''',

    # metadata for upload to PyPI
    author="Marijn van der Zee",
    author_email="marijn@serraict.com",
    description="Generate a static site from a Github wiki",
    license="Apache 2.0",
    keywords="github wiki static site html",
    url="https://github.com/serra/wiki-to-doc",
)
