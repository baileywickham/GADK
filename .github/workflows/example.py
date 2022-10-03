from workflow import *

on = On({'push': {'branches': ['main']}})
steps = [Step(Use('', 'actions/checkout@v3')),
         Step(Run('say hi', 'echo hi'))]
job = Job('build', 'ubuntu-latest', steps)
workflow = Workflow('CI', on, [job])

workflows = Workflows([workflow])
