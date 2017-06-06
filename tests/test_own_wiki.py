# -*- coding: utf-8 -*-
import context
from wikidoc import build_docs
from helpers import WikiToDocTestBase
from pytest import mark
import unittest
import os


class OwnWikiToDocTestSuite(WikiToDocTestBase):

    def test_own_wikidoc(self):
        out_dir = os.path.join(build_docs.WORKING_DIR, 'sites',
                               'wiki-to-doc.wiki')
        self._build_docs('https://github.com/serra/wiki-to-doc.wiki.git',
                         'wiki-to-doc.wiki')
        self.assert_exists(out_dir, 'Home')
        self.assert_exists(out_dir, 'Another-page')
        self.assert_exists(out_dir, 'index.html')

    @mark.slow
    def test_own_wikidoc_when_repo_already_exists(self):
        out_dir = os.path.join(build_docs.WORKING_DIR, 'sites',
                               'wiki-to-doc.wiki')
        self._build_docs('https://github.com/serra/wiki-to-doc.wiki.git',
                         'wiki-to-doc.wiki')
        self._build_docs('https://github.com/serra/wiki-to-doc.wiki.git',
                         'wiki-to-doc.wiki')
        self.assert_exists(out_dir, 'Home')

    @mark.slow
    def test_own_wikidoc_when_repo_does_not_exist(self):
        out_dir = os.path.join(build_docs.WORKING_DIR, 'sites',
                               'wiki-to-doc.wiki')
        self._build_docs('https://github.com/serra/wiki-to-doc.wiki.git',
                         'wiki-to-doc.wiki', delete_repo_dir=True)
        self.assert_exists(out_dir, 'Home')

    # additional test cases (now tested manually):
    #  - origin not set to repo url
    #  - wiki folder not a git repo


if __name__ == '__main__':
    unittest.main()
