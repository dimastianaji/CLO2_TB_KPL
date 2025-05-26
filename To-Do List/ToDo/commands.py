"""
Command Pattern: Mengenkapsulasi aksi pada task seperti complete dan expire.
"""
class CompleteTaskCommand:
    def __init__(self, task):
        self.task = task

    def execute(self):
        """Menandai task sebagai selesai."""
        self.task.complete()

class ExpireTaskCommand:
    def __init__(self, task):
        self.task = task

    def execute(self):
        """Menandai task sebagai expired."""
        self.task.expire()
