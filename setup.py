from setuptools import setup
from os import path

with open('README.rst') as f:
  long_description_contents = f.read()

setup(
  name='em7api',
  author='Doug Ip'
  version='0.1.4',
  packages=['em7api',],
  package_dir={'em7api': 'em7api'},
  long_description=long_description_contents,
  install_requires=['requests']
)

