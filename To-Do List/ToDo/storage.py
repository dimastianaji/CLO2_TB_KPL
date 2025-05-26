todo_list = []

def add_task(task):
    todo_list.append(task)

def get_all_tasks():
    return todo_list

def get_active_tasks():
    return [t for t in todo_list if t.status == 'Created']

def get_history_tasks():
    return [t for t in todo_list if t.status in ['Completed', 'Expired']]
