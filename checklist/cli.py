import click
from .checklist import load_checklist

@click.command()
def main():
    """Example script."""
    cl = load_checklist()
    for idx, w in enumerate(cl.warnings, 1):
        click.echo(f"\nWARNING {idx}: "+w)
    click.echo('\n')

    completed = {}
    for itm in cl.items:
        completed[itm] = click.confirm(itm)
    pct_complete = round(sum(completed.values())/len(completed.values())*100)
    click.echo(f'{pct_complete}% of items completed.')
