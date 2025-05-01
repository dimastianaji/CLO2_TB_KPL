import datetime

# Konfigurasi global
class Config:
    def __init__(self):
        self.time_format = "%Y-%m-%d"
        self.auto_update_status = True

config = Config()

# Model tugas
class Task:
    def __init__(self, title, deadline_str, progress=0):
        self.title = title
        self.deadline = datetime.datetime.strptime(deadline_str, config.time_format)
        self.progress = progress  # 0 - 100
        self.status = self.determine_status()

    def determine_status(self):
        if self.progress == 0:
            return "Not Started"
        elif self.progress < 100:
            return "In Progress"
        else:
            return "Completed"

    def update_progress(self, new_progress):
        if 0 <= new_progress <= 100:
            self.progress = new_progress
            if config.auto_update_status:
                self.status = self.determine_status()
        else:
            print("⚠️ Progress harus antara 0-100.")

    def is_late(self):
        return datetime.datetime.now() > self.deadline and self.status != "Completed"

    def __str__(self):
        late_flag = "⏰ TERLAMBAT" if self.is_late() else ""
        return f"{self.title} | {self.progress}% | {self.status} | Deadline: {self.deadline.strftime(config.time_format)} {late_flag}"

# Reusable function
def print_task_list(tasks):
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

# Contoh penggunaan
if __name__ == "__main__":
    tugas1 = Task("Tugas KPL", "2025-05-05")
    tugas2 = Task("Laporan Proyek", "2025-05-03", progress=50)
    tugas3 = Task("Presentasi", "2025-04-29", progress=100)

    daftar_tugas = [tugas1, tugas2, tugas3]
    print("📋 Daftar Tugas Mahasiswa:")
    print_task_list(daftar_tugas)

    print("\n🔧 Update Progress:")
    tugas1.update_progress(30)
    tugas2.update_progress(100)

    print_task_list(daftar_tugas)
