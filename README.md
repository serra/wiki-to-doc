# wiki-to-doc

Simple approach to create an offline, static copy of a github wiki that is:

 * Readable
 * Browsable
 * Searchable

See [the wiki](https://github.com/serra/wiki-to-doc/wiki) for documentation.

| OS | CI status | Python versions | Note |
|---|---|---|---|
| Linux | [![Build Status][travis-img]][travis-link] | 2.7, 3.4, 3.6 | |
| Windows | [![Windows Build status][appveyor-img]][appveyor-link] | 2.7 | See [#6] for 3.4 and 3.6 support |
| OS X | N.A. [#7] | 3.6 | Developed on OS X, Python 3.6 |

[![PyPI Version][pypi-v-image]][pypi-v-link]

[pypi-v-image]: https://img.shields.io/pypi/v/wikidoc.png
[pypi-v-link]: https://pypi.python.org/pypi/wikidoc
[travis-img]: https://travis-ci.org/serra/wiki-to-doc.svg?branch=master
[travis-link]: https://travis-ci.org/serra/wiki-to-doc
[appveyor-img]: https://ci.appveyor.com/api/projects/status/llriy5we778rua1h?svg=true
[appveyor-link]: https://ci.appveyor.com/project/serra/wiki-to-doc
[#6]: https://github.com/serra/wiki-to-doc/issues/6
[#7]: https://github.com/serra/wiki-to-doc/issues/7

## Installing

```
pip install wikidoc
wikidoc --help
```

## Usage

```
wikidoc build --repo https://github.com/serra/wiki-to-doc.wiki.git --name wiki-to-doc.wiki
ls ~/wiki-to-doc/sites
```

## Developing

Developed on OSX, Python version 3.6.

### Prepare environment

Assuming virtualenv 1.7+:

```
cd [wiki-to-doc repo]
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run tests

```
cd [wiki-to-doc repo]
pytest
```

I like to run sniffer, so that tests are automatically run when files change:

```
cd [wiki-to-doc repo]
sniffer
```

### Developing & hacking

Package using pip and setuptools. During development:

```
. venv/bin/activate
pip install --editable .

```

This gives you the virtual environment from above,
with the wikidoc package installed and editable.
This way you can experiment with the cli script from the terminal 
immediately while developing.

### Packaging

Use `bumpversion` to, well, bump the version.
This will update the version information in 

 * setup.cfg
 * setup.py
 * wikidoc/_version.py

It will add a version tag to the current commit too.

So to do a patch increment:

```
git checkout master
git pull
bumpversion patch
git push origin master --tags

```

### Publishing

Publishing is done when a version tag is pushed to Github.
This is picked up by Travis, which will do a deploy to PyPI.

Assuming pypi and pypitest configured in `~/pypirc`,
you can publish from your local machine:

```
python setup.py register -r [pypi|pypitest]
python setup.py sdist upload -r [pypi|pypitest]
```

[Peter Downs]: http://peterdowns.com/posts/first-time-with-pypi.html


