import json

class Checklist(object):
    """ Stores a checklist data parsed from a json file.
    """
    def __init__(self, warnings, items):
        self.warnings = warnings
        self.items = items

    @classmethod
    def read(cls, filepath):
        with open(filepath, "r") as f:
            data = json.load(f)

        warnings = data['warnings']
        items = data['items']

        return cls(warnings, items)
