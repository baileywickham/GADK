from __future__ import annotations
from typing import Literal, Dict, Any
import yaml


class Template:
    def __init__(self) -> None:
        # A dict which holds the data in the action
        self.data = {}

    def to_yaml(self):
        data = self.build()
        return yaml.dump(data, sort_keys=False)

    def build(self) -> Dict:
        return self.data


class On(Template):
    Triggers = Literal['push', 'pull_request']

    def __init__(self, on: Dict[Triggers, Dict[Triggers, Any]]) -> None:
        self.data = on


class Run(Template):
    def __init__(self, name: str, cmd):
        self.name = name
        self.cmd = cmd

    def build(self) -> Dict:
        return {'name': self.name, 'run': self.cmd}


class Use(Template):
    def __init__(self, name: str, uses: str):
        self.name = name
        self.uses = uses

    def build(self) -> Dict:
        return {'name': self.name, 'uses': self.uses}


class Step(Template):
    def __init__(self, data: Run | Use):
        self.data = data

    def build(self) -> Dict:
        return self.data.build()


class Job(Template):
    def __init__(self, name: str, runs_on: str, steps: list[Step]) -> None:
        self.name = name
        self.runs_on = runs_on
        self.steps = steps

    def build(self) -> Dict:
        steps = [x.build() for x in self.steps]
        body = {'runs-on': self.runs_on,
                'steps': steps}
        return {self.name: body}


class Workflow(Template):
    def __init__(self, name: str, on: On, jobs: list[Job]):
        self.name = name
        self.on = on
        self.jobs = jobs

    def build(self):
        on = self.on.build()
        jobs = {}
        for job in self.jobs:
            jobs.update(job.build())
        return {'name': self.name, 'on': on, 'jobs': jobs}


class Workflows(Template):
    def __init__(self, workflows):
        self.workflows = workflows
