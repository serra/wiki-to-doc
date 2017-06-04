# wiki-to-doc

Simple approach to create an offline, static copy of a github wiki.

See [the wiki](https://github.com/serra/wiki-to-doc/wiki) for documentation.

[![Build Status](https://travis-ci.org/serra/wiki-to-doc.svg?branch=master)](https://travis-ci.org/serra/wiki-to-doc)

## Developing

Developed using Python3; tested with Python 2.7, 3.4 and 3.6.

### Prepare environment

Assuming virtualenv 1.7+:

```
cd [wiki-to-doc repo]
virtualenv -p /usr/bin/python3.6 venv
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
$ . venv/bin/activate
$ pip install --editable .

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

It will add a tag to the current commit too.

When this tag is pushed and detected by our CI system, 
the CI system will create a release and push it to PyPi.

So to do a patch increment:

```
git checkout master
git pull
bumpversion patch
git push origin master --tags

```

#### some notes on versioning ...

Do not: 

 * set `__version__` in `__init__.py`
 * import your module code from within `setup.py`

See [here](https://stackoverflow.com/questions/2058802/how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package) 
and [here](https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package) for details.

Also interesting [PEP 396], [PEP 440] and the [bumpversion] script.

 [PEP 396]: https://www.python.org/dev/peps/pep-0396/
 [PEP 440]: https://www.python.org/dev/peps/pep-0440/
 [bumpversion]: https://pypi.python.org/pypi/bumpversion


### Publishing

Test if you can package and upload to pypitest:

```
python setup.py register -r pypitest
```

Actually upload it:

```
python setup.py sdist upload -r pypitest
```

We can do the same for PyPi:

```
python setup.py register -r pypi
```

And:

```
python setup.py sdist upload -r pypi
```

## Installing

```
pip install wikidoc
wikidoc --help
```


## Usage

```
pip install wikidoc
wikidoc --help
```

