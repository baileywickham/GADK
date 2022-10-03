import sys
import argparse
from importlib import import_module

import yaml

parser = argparse.ArgumentParser(description='Generate workflow files.')
parser.add_argument('--print', action='store_true')
parser.add_argument('file')

if __name__ == '__main__':
    args = parser.parse_args()
    mod = import_module(args.file)
    workflows = mod.workflows
    for workflow in workflows.workflows:
        yml = f'GENERATED FROM {args.file}, DO NOT EDIT DIRECTLY\n' + workflow.to_yaml()

        if args.print:
            print(workflow.to_yaml())
        else:
            with open(workflow.name + '.yaml', 'w') as f:
                f.write(workflow.to_yaml())

