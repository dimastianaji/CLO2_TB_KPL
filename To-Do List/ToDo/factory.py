"""
Factory Pattern untuk membuat instance task (TodoItem).
"""
from models import TodoItem

class TaskFactory:
    @staticmethod
    def create_task(title, deadline):
        return TodoItem(title, deadline)
