from setuptools import setup, find_packages
from setuptools.command.install import install
import re
import os

setup(
    name='checklist',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.json'],
        # And include any *.msg files found in the 'hello' package, too:
    },
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        checklist=checklist.cli:main
    ''',
)
