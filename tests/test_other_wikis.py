# -*- coding: utf-8 -*-
import context
from helpers import WikiToDocTestBase

import unittest

class OtherWikisToDocTestSuite(WikiToDocTestBase):

    def test_nlog_wikidoc(self):
        self._build_docs('https://github.com/NLog/NLog.wiki.git',
                         'NLog.wiki')

    def test_specflow_wikidoc(self):
        self._build_docs('https://github.com/techtalk/SpecFlow.wiki.git',
                         'SpecFlow.wiki')

    def test_selenium_wikidoc(self):
        self._build_docs('https://github.com/SeleniumHQ/selenium.wiki.git',
                         'selenium.wiki', 'Getting-Started')
        # note: index.html should redirect to getting started
        # for now this is a manual check


if __name__ == '__main__':
    unittest.main()
