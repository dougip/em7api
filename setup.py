from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
  long_description_contents = f.read()

setup(
  name='em7api',
  version='0.1.3',
  packages=['em7api',],
  package_dir={'em7api': 'em7api'},
  long_description=long_description_contents,
  install_requires=['requests']
)

