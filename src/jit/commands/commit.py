#!/usr/bin/env python3

import click

@click.command()
@click.option("--message", "-m", help="body of commit message, typically a description of the changes that are being committed")
def commit(message):
    click.echo("jit commit: to be implemented")