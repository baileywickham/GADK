from workflow import *

on = On({'push': ['main']})
steps = [Step({'uses': 'actions/checkout@v3'}), Step({'name': 'say hi', 'run': 'echo hi'})]
job = Job('build', 'ubuntu-latest', steps)
workflow = Workflow('CI', on, [job])

workflows = [workflow]


