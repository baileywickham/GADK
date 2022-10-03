import os
import argparse

parser = argparse.ArgumentParser(description='Generate workflow files.')
parser.add_argument('--print', action='store_true')
parser.add_argument('file')

if __name__ == '__main__':
    args = parser.parse_args()
    glbls = {}
    with open(args.file, 'r') as f:
        data = '\n'.join(f.readlines())
        exec(data, glbls)
    workflows = glbls['workflows']
    for workflow in workflows.workflows:
        yml = f'# GENERATED FROM {args.file}, DO NOT EDIT DIRECTLY\n' + workflow.to_yaml()
        if args.print:
            print(yml)
        else:
            with open(workflow.name + '.yaml', 'w') as f:
                f.write(yml)

