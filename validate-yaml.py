#! /usr/bin/env python
from __future__ import print_function
import sys
import yaml
if len(sys.argv) > 1:
    yaml_file = open(sys.argv[1])
    yaml.parse(yaml_file)
else:
    print("Usage: python validate-yaml.py input.yml")
