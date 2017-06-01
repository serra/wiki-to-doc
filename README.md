# wiki-to-doc

Simple approach to create an offline, distributable copy of a github wiki.

See [the wiki](https://github.com/serra/wiki-to-doc/wiki) for documentation.

[![Build Status](https://travis-ci.org/serra/wiki-to-doc.svg?branch=master)](https://travis-ci.org/serra/wiki-to-doc)

## Developing

Developed using Python3; tested with Python 2.7, 3.4 and 3.6.

Assuming virtualenv 1.7+:

```
cd [wiki-to-doc repo]
virtualenv -p /usr/bin/python3.4 venv
source venv/bin/activate
pip install -r requirements.txt
```

Run tests:

```
cd [wiki-to-doc repo]
pytest
```

I like to run sniffer, so that tests are automatically run when files change:
```
cd [wiki-to-doc repo]
sniffer
```


## Installing


## Usage

