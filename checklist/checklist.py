from pathlib import Path
import json

DEFAULT_CHECKLIST = Path(__file__).parent / 'assets' / 'checklist.json'

def load_checklist():
    cl = Checklist.read(DEFAULT_CHECKLIST)
    return cl

class Checklist(object):
    """ Stores a checklist data parsed from a json file.
    """
    def __init__(self, warnings, items):
        self.warnings = warnings
        self.items = items
        self.format()

    @classmethod
    def read(cls, filepath):
        with open(filepath, "r") as f:
            data = json.load(f)

        warnings = data['warnings']
        items = data['items']

        return cls(warnings, items)

    def format(self):
        self.warnings = [self.format_str(w) for w in self.warnings]
        self.items = [self.format_str(i) for i in self.items]

    def format_str(self, str, line_len = 80):
        current_line_len = 0
        lines = [[]]
        for word in str.split(' '):
            if current_line_len + len(word) > line_len:
                lines.append([])
                current_line_len = 0
            lines[-1].append(word)
            current_line_len += (len(word) + 1)
        return "\n".join([" ".join(line) for line in lines])
