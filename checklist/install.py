import os
import re

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

def appendToBashrc():
  with open(bashrc, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if pattern.match(line):
        return
    out = open(bashrc, 'a')
    out.write('\n%s' % alias)
    out.close()

if __name__ == "__main__":
  appendToBashrc()
