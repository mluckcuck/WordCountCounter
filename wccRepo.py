""" wccRepo Downloads a remote git repository and
makes a new directory for it, if required
"""

import git
import os


def makeNewDir(name):
    print("+++ Making Directory", name, "+++")

    if not os.path.exists(name):

        print("+++ Made It +++")
        os.makedirs(name)
    else:
        print("+++ Dir", name, "Already Exists +++")

        print("+++ Continue +++")


def cloneRepo(remoteUrl, directory):
    print("+++ Cloning Repo +++")
    assert os.path.exists(directory)

    if not os.path.exists(directory + "/.git"):

        git.Repo.clone_from(remoteUrl, directory)
        print("+++ Repo Cloned +++")
    else:
        print("+++ Repo Exists +++")

        print("+++ Continue +++")
