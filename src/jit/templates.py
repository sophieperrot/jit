#!/usr/bin/env python3

import yaml
import os
from pathlib import Path

def load_config(repo_path):

    global_config_path = Path.home() / ".config" / "jit" / "config.yaml"

    if global_config_path.exists():
        with open(global_config_path, 'r') as global_config_file:
            global_config = yaml.safe_load(global_config_file)

    if repo_path:
        local_config_path = Path(repo_path) / ".jit" / "config.yaml"
    else:
        local_config_path = Path.cwd() / ".jit" / "config.yaml"

    if local_config_path.exists():
        with open(local_config_path, 'r') as local_config_file:
            local_config = yaml.safe_load(local_config_file)
            if local_config:
                config = merge_configs(local_config, global_config)
