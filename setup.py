from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.0.1"
DESCRIPTION = "A package that allows for txt and md conversion to HTML files."
LONG_DESCRIPTION = (
    "A package that allows for txt and md files to be converted to HTMl files, with the option to change the stylesheet of the generated HTML page. "
    "As well as created a table of contents based on your input to the sidebar.py file."
)

# Setting up
setup(
    name="ez-txt2html",
    version=VERSION,
    author="Bryce Seefieldt",
    author_email="<bryce.seefieldt@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=[
        "python",
        "txt",
        "text",
        "md",
        "Markdown",
        "conversion",
        "HTML",
        "web-page",
        "web page",
        "TOML",
        "toml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
    ],
)