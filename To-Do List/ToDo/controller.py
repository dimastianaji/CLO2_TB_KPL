"""
Controller aplikasi: menangani logika bisnis, validasi, dan pemanggilan perintah.
"""

import datetime
from config import Config
from factory import TaskFactory
from commands import CompleteTaskCommand, ExpireTaskCommand
from storage import add_task, get_active_tasks

config = Config()

def handle_create_task(title, deadline):
    """
    Membuat task baru jika belum melebihi batas maksimum.
    """
    from storage import todo_list
    if len(todo_list) >= config.max_tasks:
        raise Exception("Maksimum jumlah task tercapai.")
    task = TaskFactory.create_task(title, deadline)
    add_task(task)
    return task

def handle_complete_task(index):
    """
    Menandai task (berdasarkan index dari task aktif) sebagai selesai.
    """
    active = get_active_tasks()
    if index < 0 or index >= len(active):
        raise IndexError("Indeks tidak valid.")
    cmd = CompleteTaskCommand(active[index])
    cmd.execute()
    return active[index]

def handle_check_deadlines(now=None):
    """
    Mengecek task yang melewati deadline dan menandai sebagai expired.
    """
    if now is None:
        now = datetime.datetime.now()
    expired = []
    for task in get_active_tasks():
        if now > task.deadline:
            cmd = ExpireTaskCommand(task)
            cmd.execute()
            expired.append(task)
    return expired
