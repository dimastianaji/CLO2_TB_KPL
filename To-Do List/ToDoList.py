import datetime
from transitions import Machine

# Konfigurasi runtime aplikasi
class Config:
    def __init__(self):
        self.time_format = "%Y-%m-%d %H:%M"   # Format waktu standar
        self.max_tasks = 10                   # Maksimum jumlah tugas
        self.enable_notifications = True      # Notifikasi diaktifkan (belum digunakan)


config = Config()

# Daftar global untuk menyimpan semua task
todo_list = []


class TodoItem:
    """
    Representasi satu item to-do.
    Setiap item memiliki judul, tenggat waktu, status, dan state machine (FSM).
    """
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = datetime.datetime.strptime(deadline, config.time_format)
        self.status = 'Created'
        self.fsm = TaskFSM(self)

    def __str__(self):
        return f"{self.title} | {self.status} | Due: {self.deadline.strftime(config.time_format)}"


class TaskFSM:
    """
    FSM (Finite State Machine) untuk mengatur status task.
    Transisi status yang didukung: Created -> Completed / Expired.
    """
    states = ['Created', 'Completed', 'Expired']

    def __init__(self, task: TodoItem):
        self.task = task
        self.machine = Machine(
            model=task,
            states=TaskFSM.states,
            initial='Created'
        )

        # Definisi transisi FSM
        self.machine.add_transition(trigger='complete', source='Created', dest='Completed', after=self.set_completed)
        self.machine.add_transition(trigger='expire', source='Created', dest='Expired', after=self.set_expired)

    def set_completed(self):
        """Atur status task menjadi Completed."""
        self.task.status = 'Completed'

    def set_expired(self):
        """Atur status task menjadi Expired."""
        self.task.status = 'Expired'


def create_task(title, deadline):
    """
    Membuat task baru dan menambahkannya ke daftar jika jumlah belum melebihi batas maksimum.
    """
    if len(todo_list) >= config.max_tasks:
        raise Exception("Maksimum jumlah task tercapai.")

    task = TodoItem(title, deadline)
    todo_list.append(task)
    return task


def get_active_tasks():
    """
    Mengembalikan daftar task yang masih aktif (status 'Created').
    """
    return [task for task in todo_list if task.status == 'Created']


def get_history_tasks():
    """
    Mengembalikan daftar task yang sudah selesai atau kedaluwarsa.
    """
    return [task for task in todo_list if task.status in ['Completed', 'Expired']]


def complete_task_by_index(index):
    """
    Menandai task tertentu (berdasarkan indeks dari daftar aktif) sebagai selesai.
    Akan melempar IndexError jika indeks tidak valid.
    """
    active_tasks = get_active_tasks()

    if index < 0 or index >= len(active_tasks):
        raise IndexError("Indeks task tidak valid.")

    task = active_tasks[index]
    task.complete()
    return task


def check_deadlines(now=None):
    """
    Mengecek semua task aktif dan menandai sebagai expired jika sudah melewati deadline.
    Mengembalikan daftar task yang ditandai expired.
    """
    if now is None:
        now = datetime.datetime.now()

    expired_tasks = []

    for task in todo_list:
        if task.status == 'Created' and now > task.deadline:
            task.expire()
            expired_tasks.append(task)

    return expired_tasks