class Storage:
    _todo_list = []

    @classmethod
    def add_task(cls, task):
        cls._todo_list.append(task)

    @classmethod
    def get_all(cls):
        return cls._todo_list

    @classmethod
    def get_active(cls):
        return [t for t in cls._todo_list if t.status == 'Created']

    @classmethod
    def get_history(cls):
        return [t for t in cls._todo_list if t.status in ['Completed', 'Expired']]
