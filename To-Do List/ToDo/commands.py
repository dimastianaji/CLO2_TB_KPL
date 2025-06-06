class CompleteTaskCommand:
    def __init__(self, task):
        self.task = task

    def execute(self):
        self.task.complete()

class ExpireTaskCommand:
    def __init__(self, task):
        self.task = task

    def execute(self):
        self.task.expire()
