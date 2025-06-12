import datetime
from memory_profiler import profile
from ToDo.config import Config
from ToDo.factory import TaskFactory
from ToDo.commands import CompleteTaskCommand, ExpireTaskCommand
from ToDo.task_storage import Storage

config = Config()

def validate_deadline(deadline_str):
    try:
        return datetime.datetime.strptime(deadline_str, config.time_format)
    except ValueError:
        raise ValueError(f"Format deadline harus sesuai {config.time_format}.")

def validate_title(title):
    title = title.strip()
    if not title:
        raise ValueError("Judul task tidak boleh kosong.")
    if len(title) > 100:
        raise ValueError("Judul task terlalu panjang (maks. 100 karakter).")
    return title

@profile
def handle_create_task(title, deadline):
    if len(Storage.get_all()) >= config.max_tasks:
        raise Exception("Maksimum jumlah task tercapai.")
    validate_deadline(deadline)
    task = TaskFactory.create_task(title, deadline)
    Storage.add_task(task)
    return task

def handle_complete_task(index):
    active = Storage.get_active()
    if not active:
        raise ValueError("Tidak ada task aktif untuk diselesaikan.")
    if index < 0 or index >= len(active):
        raise IndexError("Indeks tidak valid.")
    cmd = CompleteTaskCommand(active[index])
    cmd.execute()
    return active[index]

@profile
def handle_check_deadlines(now=None):
    if now is None:
        now = datetime.datetime.now()
    expired = []
    for task in Storage.get_active():
        if now > task.deadline:
            cmd = ExpireTaskCommand(task)
            cmd.execute()
            expired.append(task)
    return expired
