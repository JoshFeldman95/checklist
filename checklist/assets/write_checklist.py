import json
import re

def write_checklist():
    checklist = {
        'warnings': [],
        'items': []
    }

    with open("./checklist_raw.txt") as file:
        data = file.read()

    data = re.split('\n(?=[0-9b-h\\t\/]+\.)', data)

    checklist['warnings'].append('Following this checklist in no way guarantees just outcomes.')
    checklist['warnings'].append(
        ('This checklist does not reduce the need for government regulation. '
        '"Governments need to regulate AI by expanding the powers of sector-specific agencies to oversee, '
        'audit, and monitor these technologies by domain" (AI NOW 2018 Report).')
    )

    checklist['items'] = data

    with open('checklist.json', 'w') as outfile:
        json.dump(checklist, outfile)

if __name__ == "__main__":
    write_checklist()
