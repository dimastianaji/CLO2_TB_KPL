import cProfile
from TaskManager.TaskManager import Task, TaskManager

def run():
    manager = TaskManager()
    for i in range(1000):
        task = Task(f"Tugas {i}", "2025-06-20")
        manager.add_task(task)
    manager.remove_task("Tugas 500")
    manager.get_late_tasks()

if __name__ == '__main__':
    cProfile.run('run()')
