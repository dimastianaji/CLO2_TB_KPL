from ToDo.models import TodoItem

class TaskFactory:
    @staticmethod
    def create_task(title, deadline):
        return TodoItem(title, deadline)
