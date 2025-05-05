import datetime
from typing import TypeVar, Generic, List

# Konfigurasi umum: mengatur hal-hal global seperti format tanggal
class Config:
    def __init__(self):
        self.time_format = "%Y-%m-%d"  # Format tanggal
        self.auto_update_status = True  # status berubah otomatis saat progress berubah

config = Config()

# Tipe generik untuk class Manager
T = TypeVar('T')

# Kelas Manager 
class Manager(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def add(self, item: T):
        self.items.append(item)

    def remove(self, item: T):
        self.items.remove(item)

    def get_all(self) -> List[T]:
        return self.items

# Class Task menyimpan info tentang suatu tugas
class Task:
    def __init__(self, title, deadline_str, progress=0):
        self.title = title
        self.deadline = datetime.datetime.strptime(deadline_str, config.time_format)
        self.progress = progress
        self.status = self.determine_status()

    # Cek status berdasarkan progress
    def determine_status(self):
        if self.progress == 0:
            return "Not Started"
        elif self.progress < 100:
            return "In Progress"
        else:
            return "Completed"

    # Update progress tugas
    def update_progress(self, new_progress):
        if 0 <= new_progress <= 100:
            self.progress = new_progress
            if config.auto_update_status:
                self.status = self.determine_status()
        else:
            print(" Progress harus antara 0-100.")

    # Cek apakah tugas sudah lewat deadline atau belum selesai
    def is_late(self):
        return datetime.datetime.now() > self.deadline and self.status != "Completed"

    # Cara tampilkan info tugas dalam bentuk string
    def __str__(self):
        late_flag = "⏰ TERLAMBAT" if self.is_late() else ""
        return f"{self.title} | {self.progress}% | {self.status} | Deadline: {self.deadline.strftime(config.time_format)} {late_flag}"

# TaskManager ini khusus buat ngatur kumpulan tugas (berbasis class Task)
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    # Ambil daftar tugas yang lewat deadline
    def get_late_tasks(self):
        return [task for task in self.tasks if task.is_late()]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.status == "Completed"]

    def get_in_progress_tasks(self):
        return [task for task in self.tasks if task.status == "In Progress"]

    # Tampilkan semua tugas
    def print_all_tasks(self):
        if not self.tasks:
            print(" Tidak ada tugas.")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

    # Update progress tugas berdasarkan judulnya
    def update_task_progress(self, title, new_progress):
        for task in self.tasks:
            if task.title == title:
                task.update_progress(new_progress)
                return
        print(" Tugas tidak ditemukan.")

# Menu pilihan buat user
def show_menu():
    print("\nMenu:")
    print("1. Lihat Semua Tugas")
    print("2. Lihat Tugas Yang Selesai")
    print("3. Lihat Tugas Yang Belum Selesai")
    print("4. Update Progress Tugas")
    print("5. Keluar")

# Program utama dijalankan dari sini
def main():
    manager = TaskManager()

    # Tambah beberapa tugas sebagai contoh awal
    tugas1 = Task("Tugas KPL", "2025-05-05")
    tugas2 = Task("Laporan Proyek", "2025-05-03", progress=50)
    tugas3 = Task("Presentasi", "2025-04-29", progress=100)
    manager.add_task(tugas1)
    manager.add_task(tugas2)
    manager.add_task(tugas3)

    # Loop menu utama
    while True:
        show_menu()
        choice = input("Pilih opsi (1-5): ")

        if choice == "1":
            print("\n Daftar Semua Tugas:")
            manager.print_all_tasks()
        elif choice == "2":
            print("\n Tugas Selesai:")
            completed_tasks = manager.get_completed_tasks()
            if completed_tasks:
                for task in completed_tasks:
                    print(f"- {task.title}")
            else:
                print(" Tidak ada tugas yang selesai.")
        elif choice == "3":
            print("\n Tugas Yang Belum Selesai:")
            in_progress_tasks = manager.get_in_progress_tasks()
            if in_progress_tasks:
                for task in in_progress_tasks:
                    print(f"- {task.title}")
            else:
                print(" Tidak ada tugas yang sedang berjalan.")
        elif choice == "4":
            title = input("Masukkan judul tugas yang ingin diupdate: ")
            new_progress = int(input("Masukkan progress baru (0-100): "))
            manager.update_task_progress(title, new_progress)
        elif choice == "5":
            print("Keluar dari program.")
            break
        else:
            print(" Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program kalau file ini langsung dibuka
if __name__ == "__main__":
    main()
