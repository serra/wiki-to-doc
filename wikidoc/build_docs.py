#!/usr/bin/env python2
# -*- coding: utf-8 -*- #
#
# Builds the GitHub Wiki documentation into a static HTML site.
#
# Copyright (c) 2015 carlosperate https://github.com/carlosperate/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This script does the following to build the documentation:
#    Pulls the latest changes from the GitHub Wiki repository
#    Edits the MkDocs configuration file to include all the markdown files
#    Creates an index.html file to have root redirected to a specific page
#    Builds the static site using MkDocs
#    REMOVES the root Documentation folder
#    Copies the generate content into the root Documentation folder
#
from __future__ import unicode_literals, absolute_import
import os
import sys
import subprocess
import yaml

# mkdocs used only in the command line, imported just to ensure it's installed
try:
    import mkdocs
except ImportError:
    print("You need to have mkdocs installed !")
    sys.exit(1)

from os.path import expanduser
home = expanduser("~")

MKDOCS_FOLDER = "mkdocs"
WORKING_DIR = os.path.join(home, "wiki-to-doc")
MKDOCS_DIR = os.path.join(WORKING_DIR, MKDOCS_FOLDER)

DEFAULT_INDEX = 'Home'


class Error(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class DocBuilder(object):

    def __init__(self, github_wiki_repo, wiki_name,
                 index=DEFAULT_INDEX):
        # Path data
        self._wiki_name = wiki_name
        self._github_wiki_repo = github_wiki_repo
        self._out_dir = os.path.join(WORKING_DIR, 'sites', self._wiki_name)
        self._index = index

    def pull_wiki_repo(self):
        """
        Pulls latest changes from the wiki repo.
        """
        # Set working directory to the wiki repository
        wiki_folder = os.path.join(MKDOCS_DIR, self._wiki_name)
        if os.path.isdir(wiki_folder):
            os.chdir(wiki_folder)
        else:
            self.clone_repo(wiki_folder)
            os.chdir(wiki_folder)

        self.ensure_correct_repository(wiki_folder)

        # Git Fetch prints progress in stderr, so cannot check for erros that
        # way
        subprocess.call(["git", "pull", "origin", "master"])

    def clone_repo(self, wiki_folder):
        subprocess.call(["git", "clone", self._github_wiki_repo, wiki_folder])

    def ensure_correct_repository(self, wiki_folder):
        pipe = subprocess.PIPE
        git_process = subprocess.Popen(
            ["git", "config", "--get", "remote.origin.url"],
            stdout=pipe, stderr=pipe)
        std_op, std_err_op = git_process.communicate()

        if std_err_op:
            raise Error("Could not get the remote information from the wiki "
                        "repository !\n%s" + std_err_op)

        if self._github_wiki_repo not in str(std_op):
            raise Error(("Wiki repository:\n\t%s\n" % self._github_wiki_repo) +
                        "not found in directory %s url:\n\t%s\n" %
                        (wiki_folder, std_op))

    def edit_mkdocs_config(self):
        """
        Create mkdocs.yml file from metadata
        :return: Boolean indicating the success of the operation.
        """
        mkdocs_yml = os.path.join(MKDOCS_DIR, "mkdocs.yml")

        cfg = dict(
            site_name=self._wiki_name,
            theme='readthedocs',
            docs_dir=self._wiki_name,
            site_dir=self._out_dir
        )

        with open(mkdocs_yml, 'w') as outfile:
            yaml.dump(cfg, outfile, default_flow_style=False)

    def create_index(self):
        """
        Creates an HTML index page to redirect to an MkDocs generated page.
        """
        html_code = \
            "<!DOCTYPE HTML>\n " \
            "<html>\n" \
            "\t<head>\n" \
            "\t\t<meta charset=\"UTF-8\">\n" \
            "\t\t<meta http-equiv=\"refresh\" content=\"1;url=%s/index.html\">\n" \
            % self._index + \
            "\t\t<script type=\"text/javascript\">\n" \
            "\t\t\twindow.location.href = \"%s/index.html\"\n" % self._index +\
            "\t\t</script>\n" \
            "\t</head>\n" \
            "\t<body>\n" \
            "\t\tIf you are not redirected automatically to the " \
            "%s page, follow this <a href=\"%s/index.html\">link</a>\n"\
            % (self._index, self._index) + \
            "\t</body>\n" \
            "</html>\n"

        file_name = os.path.join(self._out_dir, "index.html")

        if not os.path.exists(file_name):
            with open(file_name, "w") as index_file:
                index_file.write(html_code)

    def build_mkdocs(self):
        """
        Invokes MkDocs to build the static documentation and moves the folder
        into the project root folder.
        """
        # Setting the working directory
        os.chdir(MKDOCS_DIR)

        # Building the MkDocs project
        pipe = subprocess.PIPE
        mkdocs_process = subprocess.Popen(
            ["mkdocs", "build", "-q"], stdout=pipe, stderr=pipe)
        std_op, std_err_op = mkdocs_process.communicate()

        if std_err_op:
            raise Error("Could not build MkDocs !\n%s" %
                        std_err_op)

    def build_docs(self):
        """ Builds the documentation HTML pages from the Wiki repository. """
        self.pull_wiki_repo()
        self.edit_mkdocs_config()
        self.build_mkdocs()
        self.create_index()


def build(
        github_wiki_repo="https://github.com/serra/wiki-to-doc.wiki.git",
        wiki_name="wiki-to-doc.wiki",
        index=DEFAULT_INDEX):
    b = DocBuilder(github_wiki_repo, wiki_name, index)
    b.build_docs()
