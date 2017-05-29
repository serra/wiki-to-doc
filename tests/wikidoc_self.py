# -*- coding: utf-8 -*-
import context
from wikidoc import build_docs

import unittest
import shutil
import os

_out_dir = build_docs.OUT_DIR


class OwnWikiToDocTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_write_pdf(self):
        shutil.rmtree(_out_dir, ignore_errors=True)
        build_docs.build_docs()
        index_file = os.path.join(_out_dir, 'index.html')
        assert os.path.exists(index_file)


if __name__ == '__main__':
    unittest.main()
