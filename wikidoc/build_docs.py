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

# Path data
GITHUB_USER = "serra"
WIKI_NAME = "wiki-to-doc.wiki"
GITHUB_WIKI_REPO = "github.com/%s/%s.git" % (GITHUB_USER, WIKI_NAME)

MKDOCS_FOLDER = "mkdocs"
WORKING_DIR = os.path.join(home, "wiki-to-doc")
MKDOCS_DIR = os.path.join(WORKING_DIR, MKDOCS_FOLDER)

DEFAULT_INDEX = 'Home'

OUT_DIR = os.path.join(WORKING_DIR, 'sites', WIKI_NAME)


class Error(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def pull_wiki_repo():
    """
    Pulls latest changes from the wiki repo.
    """
    # Set working directory to the wiki repository
    wiki_folder = os.path.join(MKDOCS_DIR, WIKI_NAME)
    if os.path.isdir(wiki_folder):
        os.chdir(wiki_folder)
    else:
        raise Error("Wiki repo directory is not correct: %s" %
                    wiki_folder)

    # Ensure the subfolder selected is the correct repository
    pipe = subprocess.PIPE
    git_process = subprocess.Popen(
        ["git", "config", "--get", "remote.origin.url"],
        stdout=pipe, stderr=pipe)
    std_op, std_err_op = git_process.communicate()

    if std_err_op:
        raise Error("Could not get the remote information from the wiki "
                    "repository !\n%s" + std_err_op)

    if GITHUB_WIKI_REPO not in std_op:
        raise Error(("ERROR: Wiki repository:\n\t%s\n" % GITHUB_WIKI_REPO) +
                    "not found in directory %s url:\n\t%s\n" %
                    (wiki_folder, std_op))

    # Git Fetch prints progress in stderr, so cannot check for erros that way
    subprocess.call(["git", "pull", "origin", "master"])


def edit_mkdocs_config():
    """
    Create mkdocs.yml file from metadata
    :return: Boolean indicating the success of the operation.
    """
    mkdocs_yml = os.path.join(MKDOCS_DIR, "mkdocs.yml")

    cfg = dict(
        site_name=WIKI_NAME,
        docs_dir=WIKI_NAME,
        site_dir=OUT_DIR
    )

    with open(mkdocs_yml, 'w') as outfile:
        yaml.dump(cfg, outfile, default_flow_style=False)


def create_index():
    """
    Creates an HTML index page to redirect to an MkDocs generated page.
    """
    html_code = \
        "<!DOCTYPE HTML>\n " \
        "<html>\n" \
        "\t<head>\n" \
        "\t\t<meta charset=\"UTF-8\">\n" \
        "\t\t<meta http-equiv=\"refresh\" content=\"1;url=%s/index.html\">\n" \
        % DEFAULT_INDEX + \
        "\t\t<script type=\"text/javascript\">\n" \
        "\t\t\twindow.location.href = \"%s/index.html\"\n" % DEFAULT_INDEX +\
        "\t\t</script>\n" \
        "\t</head>\n" \
        "\t<body>\n" \
        "\t\tIf you are not redirected automatically to the " \
        "%s page, follow this <a href=\"%s/index.html\">link</a>\n"\
        % (DEFAULT_INDEX, DEFAULT_INDEX) + \
        "\t</body>\n" \
        "</html>\n"

    print("Creating the index.html file...\n")
    generated_site_dir = OUT_DIR
    if not os.path.exists(generated_site_dir):
        os.makedirs(generated_site_dir)

    index_file = open(os.path.join(generated_site_dir, "index.html"), "w")
    index_file.write(html_code)
    index_file.close()


def build_mkdocs():
    """
    Invokes MkDocs to build the static documentation and moves the folder
    into the project root folder.
    :return: Boolean indicating the success of the operation.
    """
    # Setting the working directory
    if os.path.isdir(MKDOCS_DIR):
        os.chdir(MKDOCS_DIR)
    else:
        print("ERROR: MkDocs directory is not correct: %s" % MKDOCS_DIR)
        return False

    # Building the MkDocs project
    pipe = subprocess.PIPE
    mkdocs_process = subprocess.Popen(
        ["mkdocs", "build", "-q"], stdout=pipe, stderr=pipe)
    std_op, std_err_op = mkdocs_process.communicate()

    if std_err_op:
        print("ERROR: Could not build MkDocs !\n%s" %
              std_err_op)
        return False
    else:
        print(std_op)

    return True


def build_docs():
    """ Builds the documentation HTML pages from the Wiki repository. """
    success = pull_wiki_repo()
    if success is False:
        sys.exit(1)

    success = edit_mkdocs_config()
    if success is False:
        sys.exit(1)

    # Create index.html before the MkDocs site is created in case the project
    # already contains an index file.
    success = create_index()
    if success is False:
        sys.exit(1)

    success = build_mkdocs()
    if success is False:
        sys.exit(1)
    print("Build process finished!")


if __name__ == "__main__":
    build_docs()
