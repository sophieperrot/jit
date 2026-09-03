#!/usr/bin/env python3

import click

@click.command(help="file(s)/folder(s) to be ignored in jit status (when showing changes to commit)")
@click.argument("filepaths", help="path to file(s)/folder(s) to be ignored")
@click.argument("--undo", "-u", help="undo ignoring a file, will remove it from all ignored unless specified tag(s) to be unignored from")
@click.option("--tags", "-t", help="tag the file(s)/folder(s) to be ignored to one or more categories")
def ignore(filepaths, undo, tags):
    click.echo("jit ignore: to be implemented")

    IGNORE_FILEPATH = "jitignore.yaml"
    if undo is not None:
        undo_ignore(IGNORE_FILEPATH, filepaths, tags)
    else:
        add_ignore(IGNORE_FILEPATH, filepaths, tags)

def undo_ignore(ignore_filepath, filepaths, tags):
    pass

def add_ignore(ignore_filepath, filepaths, tags):
    if tags is not None:
        pass
    pass


    # with open(IGNORE_FILEPATH) as ignore_file:
        # for filepath in filepaths:
            # if undo
                # if file was not already ignore / filepath is invalid, show error
                # if file was previously ignored 
            # if tags
                # if file not already ignored, add to the tags' list
                # if the file previously ignored but doesn't have any tags, remove from default and list under tag
                # if the file previously ignored and already under other tags, add to under new tag (and keep its spot under the others)
            
            # if the file is not already ignored and is not tagged, add to always/default/no-tag
            # if the file is already ignored but did not have this current tag, 