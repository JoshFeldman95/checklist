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
