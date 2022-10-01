from workflow import *

on = On({'push': ['main']})
steps = [Step({'uses': 'actions/checkout@v3'})]
job = Job('build', 'ubuntu-latest', steps)
workflow = Workflow('CI', on, [job])

print(workflow.to_yaml())


