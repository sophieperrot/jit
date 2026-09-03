#!/usr/bin/env python3

import click

@click.command()
@click.option("--include", "-i", help="show an ignore category")
def status(include):
    click.echo("jit status: to be implemented")
