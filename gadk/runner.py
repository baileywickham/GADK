import os
import sys
import argparse
from importlib import import_module

import yaml

from gadk.workflow import Workflows

parser = argparse.ArgumentParser(description='Generate workflow files.')
parser.add_argument('--print', action='store_true')
parser.add_argument('file')

if __name__ == '__main__':
    args = parser.parse_args()
    glbls = {}
    print(os.listdir())
    with open(args.file, 'r') as f:
        data = '\n'.join(f.readlines())
        exec(data, glbls)
    workflows: Workflows = glbls['workflows']
    for workflow in workflows.workflows:
        yml = f'# GENERATED FROM {args.file}, DO NOT EDIT DIRECTLY\n' + workflow.to_yaml()

        if args.print:
            print(yml)
        else:
            with open(workflow.name + '.yaml', 'w') as f:
                f.write(yml)

