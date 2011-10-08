
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nbugtrack",
    version = "0.1",
    author = "Satish Srinivasan (0xhe)",
    author_email = "sathyasvasan@gmail.com",
    description = ("A Simple bugtracker for personal projects using python"),
    license = "BSD",
    keywords = "bugtracker wsgi sqlite",
    url = "http://github.com/0xhe/nbugtrack",
    packages = ['nbugtrack']
    long_description = read('README.md')
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: BSD License",
    ],
)


