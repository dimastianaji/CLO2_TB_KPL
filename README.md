 1. Singleton Pattern – Config
Digunakan agar hanya ada satu objek konfigurasi global di seluruh aplikasi.

python

class Config:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.time_format = "%Y-%m-%d"
            cls._instance.auto_update_status = True
        return cls._instance

 2. Strategy Pattern – StatusStrategy
Memisahkan logika penentuan status tugas berdasarkan progress.

python

class StatusStrategy:
    def get_status(self, progress): pass

class DefaultStatusStrategy(StatusStrategy):
    def get_status(self, progress):
        if progress == 0: return "Not Started"
        elif progress < 100: return "In Progress"
        else: return "Completed"
Digunakan di class Task:

python

class Task:
    def __init__(..., status_strategy=None):
        ...
        self.status_strategy = status_strategy or DefaultStatusStrategy()
        self.status = self.status_strategy.get_status(progress)

 3. Factory Pattern – TaskFactory
Untuk menyederhanakan dan standarisasi pembuatan objek Task.

python

class TaskFactory:
    def create_task(self, title, deadline_str, progress=0):
        return Task(title, deadline_str, progress)

✅ Contoh Pemakaian di main()
python

task_factory = TaskFactory()
tugas1 = task_factory.create_task("Tugas KPL", "2025-05-05")
