import datetime
from transitions import Machine

# Runtime Configuration Class
class Config:
    def __init__(self):
        self.time_format = "%Y-%m-%d %H:%M"
        self.max_tasks = 10
        self.enable_notifications = True

config = Config()

# TodoItem + FSM
class TodoItem:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = datetime.datetime.strptime(deadline, config.time_format)
        self.status = 'Created'
        self.fsm = TaskFSM(self)

    def __str__(self):
        return f"{self.title} | {self.status} | Due: {self.deadline.strftime(config.time_format)}"

class TaskFSM:
    states = ['Created', 'Completed', 'Expired']

    def __init__(self, task: TodoItem):
        self.task = task
        self.machine = Machine(model=task, states=TaskFSM.states, initial='Created')
        self.machine.add_transition(trigger='complete', source='Created', dest='Completed', after=self.set_completed)
        self.machine.add_transition(trigger='expire', source='Created', dest='Expired', after=self.set_expired)

    def set_completed(self):
        self.task.status = 'Completed'

    def set_expired(self):
        self.task.status = 'Expired'


# Task List Management
todo_list = []

def add_task():
    if len(todo_list) >= config.max_tasks:
        print("❌ Maksimum jumlah task tercapai.")
        return

    title = input("Judul tugas: ")
    deadline = input(f"Deadline (format: {config.time_format}): ")
    try:
        task = TodoItem(title, deadline)
        todo_list.append(task)
        print("✅ Task berhasil ditambahkan!\n")
    except ValueError:
        print("⚠️ Format deadline tidak sesuai.\n")

def show_tasks():
    active_tasks = [t for t in todo_list if t.status == 'Created']
    if not active_tasks:
        print("📭 Tidak ada tugas aktif.\n")
    else:
        print("\n📋 Tugas Aktif:")
        for i, t in enumerate(active_tasks):
            print(f"{i+1}. {t}")
        print()

def show_task_history():
    history_tasks = [t for t in todo_list if t.status in ['Completed', 'Expired']]
    if not history_tasks:
        print("📦 Belum ada riwayat tugas.\n")
    else:
        print("\n📜 Riwayat Tugas:")
        for i, t in enumerate(history_tasks):
            print(f"{i+1}. {t}")
        print()

def complete_task():
    created_tasks = [t for t in todo_list if t.status == 'Created']
    if not created_tasks:
        print("🚫 Tidak ada task yang bisa diselesaikan.\n")
        return
    for i, t in enumerate(created_tasks):
        print(f"{i+1}. {t}")
    idx = input("Masukkan nomor task yang ingin diselesaikan: ")
    try:
        i = int(idx) - 1
        task = created_tasks[i]
        task.complete()
        print("✅ Task ditandai selesai!\n")
    except:
        print("⚠️ Gagal menyelesaikan task.\n")

def check_deadlines():
    now = datetime.datetime.now()
    expired = 0
    for task in todo_list:
        if task.status == 'Created' and now > task.deadline:
            task.expire()
            expired += 1
            print(f"😱 Task '{task.title}' telah lewat deadline.")
    if expired == 0:
        print("⏰ Tidak ada task yang expired.\n")
    else:
        print()

# Menu Utama
def main():
    print("📝 Aplikasi To-Do List FSM (Tanpa fitur Mulai)\n")

    while True:
        print("Menu:")
        print("1. Tambah task")
        print("2. Lihat semua task aktif")
        print("3. Tandai task selesai")
        print("4. Cek deadline")
        print("5. Lihat riwayat tugas")
        print("0. Keluar")
        pilihan = input("Pilih menu (0-5): ")

        if pilihan == '1':
            add_task()
        elif pilihan == '2':
            show_tasks()
        elif pilihan == '3':
            complete_task()
        elif pilihan == '4':
            check_deadlines()
        elif pilihan == '5':
            show_task_history()
        elif pilihan == '0':
            print("👋 Keluar dari program.")
            break
        else:
            print("⚠️ Menu tidak valid.\n")

if __name__ == "__main__":
    main()
