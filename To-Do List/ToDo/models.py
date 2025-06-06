"""
Model untuk TodoItem dan FSM (Finite State Machine).
Menggunakan State Pattern dengan library 'transitions'.
"""

import datetime
from transitions import Machine
from config import Config

config = Config()

class TodoItem:
    """
    Representasi satu item to-do.
    Setiap task memiliki judul, deadline, status awal, dan FSM untuk transisi status.
    """
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = datetime.datetime.strptime(deadline, config.time_format)
        self.status = 'Created'
        self.fsm = TaskFSM(self)

    def __str__(self):
        return f"{self.title} | {self.status} | Due: {self.deadline.strftime(config.time_format)}"

class TaskFSM:
    """
    FSM (Finite State Machine) untuk transisi status task.
    Status: Created -> Completed / Expired
    """
    states = ['Created', 'Completed', 'Expired']

    def __init__(self, task: TodoItem):
        self.task = task
        self.machine = Machine(model=task, states=TaskFSM.states, initial='Created')
        self.machine.add_transition('complete', 'Created', 'Completed', after=self.set_completed)
        self.machine.add_transition('expire', 'Created', 'Expired', after=self.set_expired)

    def set_completed(self):
        """Mengubah status menjadi 'Completed' setelah transisi."""
        self.task.status = 'Completed'

    def set_expired(self):
        """Mengubah status menjadi 'Expired' setelah transisi."""
        self.task.status = 'Expired'
