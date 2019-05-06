from setuptools import setup, find_packages
from setuptools.command.install import install
import re
import os

class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        print("Hello, developer, how are you? :)")
        alias = """
        # adds checklist to git push
        function git {
          if [[ "$1" == "push" && "$@" != *"--help"* ]]; then
            shift 1
            command checklist
            command git push "$@"
          else
            command git "$@"
          fi
        }
        """
        pattern = re.compile(alias)

        homefolder = os.path.expanduser('~')
        bashrc = os.path.abspath('%s/.bash_profile' % homefolder)
        with open(bashrc, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if pattern.match(line):
                    return
            out = open(bashrc, 'a')
            out.write('\n%s' % alias)
            out.close()
        install.run(self)

setup(
    name='checklist',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        checklist=checklist.cli:main
    ''',
    cmdclass={
        'install': CustomInstallCommand,
    },
)
