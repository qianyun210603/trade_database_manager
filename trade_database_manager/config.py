import os

from ruamel.yaml import YAML

yaml = YAML(typ="safe")

with open(os.path.join(os.path.expanduser("~/.tradedbmgr/config.yaml")), "r") as f:
    CONFIG = yaml.load(f)
