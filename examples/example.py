from workflow import *

on = On({'push': {'branches': ['main']}})
steps = [Step(Uses('actions/checkout@v3')),
         Step(Run(name='say hi', run='echo hi'))]
job = Job('build', 'ubuntu-latest', steps)
workflow = Workflow('CI', on, [job])

workflows = Workflows([workflow])
