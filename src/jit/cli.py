#!/usr/bin/env python3

import click

from commands.status import status
from commands.commit import commit
from commands.ignore import ignore

@click.group()
def cli():
    click.echo("welcome to jit!")

cli.add_command(status)
cli.add_command(commit)
cli.add_command(ignore)