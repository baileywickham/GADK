from enum import Enum
from typing import Literal, Dict
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

    def __init__(self, on: Dict[Triggers, list[str]]) -> None:
        self.data = on


class Step(Template):
    def __init__(self, data: Dict[str, str]):
        self.data = data


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
