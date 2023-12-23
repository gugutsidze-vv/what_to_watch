import csv
import click

from . import app, db
from .models import Opinion


@app.cli.command('load_options')
def load_options_command():
    with open('opinions.csv', encoding='utf-8') as f:
        counter = 0
        for row in csv.DictReader(f):
            opinion = Opinion(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено мнений: {counter}')
