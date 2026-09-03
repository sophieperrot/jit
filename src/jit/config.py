#!/usr/bin/env python3

import yaml
from pathlib import Path

default_global_config_filepath = Path.home() / ".config" / "jit" / "config.yaml"

FALLBACK_CONFIG = {
    "commit": {
        "actions": [],
        "scopes": [],
        "template": ""
    },
    "remote": {
        "auto_push": False,
        "auto_pull": False
    },
    "safety": {
        "create_backup": True,
        "backup_prefix": "backup/"
    }
}


def merge_dict(override, base):

    merged = base.copy()

    for key, value in override.items():
        if key in merged and isinstance(value, dict) and isinstance(merged[key], dict):
            merged[key] = merge_dict(value, merged[key])
        else:
            merged[key] = value

    return merged


def load_config(repo_path, global_config_filepath = default_global_config_filepath):

    if global_config_filepath.exists():
        with open(global_config_filepath, 'r') as global_config_file:
            global_config = yaml.safe_load(global_config_file)
            if global_config:
                config = merge_dict(global_config, FALLBACK_CONFIG)

    if repo_path:
        local_config_filepath = Path(repo_path) / ".jit" / "config.yaml"
    else:
        local_config_filepath = Path.cwd() / ".jit" / "config.yaml"

    if local_config_filepath.exists():
        with open(local_config_filepath, 'r') as local_config_file:
            local_config = yaml.safe_load(local_config_file)
            if local_config:
                config = merge_dict(local_config, global_config)


def update_global_config_filepath(new_path):
    global default_global_config_filepath
    if new_path.exists():
        default_global_config_filepath = Path(new_path) / "config.yaml"
    else:
        raise NotADirectoryError