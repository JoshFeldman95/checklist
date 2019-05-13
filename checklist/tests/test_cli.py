from click.testing import CliRunner
from ..cli import main
import json

def test_main():
    with open('checklist_out.txt') as f:
        checklist_ideal = f.read()
    runner = CliRunner()
    result = runner.invoke(main)
    assert result.exit_code == 0

    lines_real = result.output.split('\n')
    lines_ideal = checklist_ideal.split('\n')
    for idx in range(len(lines_real)):
        assert lines_real[idx].strip() == lines_ideal[idx].strip()
