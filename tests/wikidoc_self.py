# -*- coding: utf-8 -*-
import context
from wikidoc import build_docs

import unittest
import shutil
import os

_out_dir = build_docs.OUT_DIR


class OwnWikiToDocTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_own_wikidoc(self):
        shutil.rmtree(_out_dir, ignore_errors=True)
        build_docs.build_docs()
        self.assert_exists('index.html')
        self.assert_exists('Home')
        self.assert_exists('Another-page')

    def assert_exists(self, rel_path):
        p = os.path.join(_out_dir, rel_path)
        assert os.path.exists(p)


if __name__ == '__main__':
    unittest.main()
