# -*- coding: utf-8 -*-
import context
from wikidoc import build_docs
from helpers import WikiToDocTestBase

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


if __name__ == '__main__':
    unittest.main()
