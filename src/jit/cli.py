#!/usr/bin/env python3

import click

from .commands.status import status
from .commands.commit import commit
from .commands.ignore import ignore


"""
1. jit or jit init -> show welcome message (can disable in config after the initial call)
2. check if this is a git repo -> if not, initialise git (guide through process of git config and setting remote / cloning repo)
3. if it is -> display starter/features/short help, create local config file
4. scan repo to add filenames for jit status
"""

@click.group()
def cli():
    click.echo("welcome to jit!")
    

cli.add_command(status)
cli.add_command(commit)
cli.add_command(ignore)