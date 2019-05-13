from ..checklist import load_checklist, Checklist
from pathlib import Path
import json

DEFAULT_CHECKLIST = Path(__file__).parent.parent / 'assets' / 'checklist.json'

def test_load_checklist():
    cl = load_checklist()

    with open(DEFAULT_CHECKLIST, "r") as f:
        data = json.load(f)

    warnings = data['warnings']
    items = data['items']

    assert cl.warnings == warnings
    assert cl.items == items

def test_Checklist():
    cl = Checklist.read(DEFAULT_CHECKLIST)

    with open(DEFAULT_CHECKLIST, "r") as f:
        data = json.load(f)

    warnings = data['warnings']
    items = data['items']

    assert cl.warnings == warnings
    assert cl.items == items
