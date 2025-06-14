import datetime
from config import time_format
from task_fsm import buat_fsm

class TodoItem:
    pass

# Testing manual (optional)
judul = input("Judul task contoh: ")
deadline_input = input(f"Deadline (format {time_format}): ")
deadline = datetime.datetime.strptime(deadline_input, time_format)

task = TodoItem()
task.title = judul
task.deadline = deadline
task.status = 'Created'
task.fsm = buat_fsm(task)

print(f"✅ Task dibuat: {task.title} | {task.deadline}")
