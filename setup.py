from setuptools import setup
from setuptools import find_packages

__version__ = '0.1.0'

setup(
    name='wikidoc',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        wikidoc=wikidoc.main:cli
    ''',
)
