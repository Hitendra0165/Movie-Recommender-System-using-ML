from setuptools import setup


with open("README.md", "r",encoding ="utf-8") as fh:
    long_description = fh.read()


AUTHOR_NAME = "Hitendra Bhamare"
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlite']

setup(
    name = SRC_REPO,
    version= '0.0.1',
    author  = AUTHOR_NAME,
    author_email= 'hitendrabhamare007@gmail.com',
    description= 'A small example package for movies recommendation',
    long_description= long_description,
    long_description_content_type = 'text/plain',
    package = [SRC_REPO],
    python_requires = '>=3.10',
    install_requires = LIST_OF_REQUIREMENTS  
)
