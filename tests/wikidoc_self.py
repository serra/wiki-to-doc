# -*- coding: utf-8 -*-
import context
from wikidoc import build_docs

import unittest
import shutil
import os


class WikiToDocTestBase(unittest.TestCase):

    def _build_docs(self, repo, name):
        out_dir = os.path.join(build_docs.WORKING_DIR, 'sites',
                               name)
        shutil.rmtree(out_dir, ignore_errors=True)
        build_docs.build_docs(repo, name)

    def assert_exists(self, out_dir, rel_path):
        p = os.path.join(out_dir, rel_path)
        assert os.path.exists(p)


class OwnWikiToDocTestSuite(WikiToDocTestBase):

    def test_own_wikidoc(self):
        out_dir = os.path.join(build_docs.WORKING_DIR, 'sites',
                               'wiki-to-doc.wiki')
        self._build_docs('https://github.com/serra/wiki-to-doc.wiki.git',
                         'wiki-to-doc.wiki')
        self.assert_exists(out_dir, 'Home')
        self.assert_exists(out_dir, 'Another-page')
        self.assert_exists(out_dir, 'index.html')


# class OtherWikisToDocTestSuite(WikiToDocTestBase):

#     def test_nlog_wikidoc(self):
#         self._build_docs('https://github.com/NLog/NLog.wiki.git',
#                          'NLog.wiki')

#     def test_specflow_wikidoc(self):
#         self._build_docs('https://github.com/techtalk/SpecFlow.wiki.git',
#                          'SpecFlow.wiki')

#     def test_selenium_wikidoc(self):
#         self._build_docs('https://github.com/SeleniumHQ/selenium.wiki.git',
#                          'selenium.wiki')


if __name__ == '__main__':
    unittest.main()
