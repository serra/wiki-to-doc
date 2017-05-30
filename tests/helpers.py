# -*- coding: utf-8 -*-
import context
from wikidoc import build_docs

import unittest
import shutil
import os


class WikiToDocTestBase(unittest.TestCase):

    def _build_docs(self, repo, name, index=build_docs.DEFAULT_INDEX):
        out_dir = os.path.join(build_docs.WORKING_DIR, 'sites',
                               name, index)
        shutil.rmtree(out_dir, ignore_errors=True)
        build_docs.build_docs(repo, name, index)

    def assert_exists(self, out_dir, rel_path):
        p = os.path.join(out_dir, rel_path)
        assert os.path.exists(p)
