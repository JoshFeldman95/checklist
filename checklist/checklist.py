from pathlib import Path
from .parser import Checklist

DEFAULT_CHECKLIST = Path(__file__).parent / 'assets' / 'checklist.json'

def load_checklist():
    cl = Checklist.read(DEFAULT_CHECKLIST)
    return cl
