# Kelas Task
class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.status = 'Pending'

    def update_status(self, new_status):
        if new_status in ['Pending', 'In Progress', 'Completed']:
            self.status = new_status
        else:
            print("⚠️ Status tidak valid!")

    def __str__(self):
        return f'Task: {self.name}, Deadline: {self.deadline}, Status: {self.status}'

# Kelas Schedule
class Schedule:
    def __init__(self):
        self.classes = []
        self.tasks = []

    def add_class(self, class_name, time):
        self.classes.append((class_name, time))

    def add_task(self, task):
        self.tasks.append(task)

    def show_schedule(self):
        print("\n📅 Jadwal Kuliah:")
        if not self.classes:
            print("Belum ada jadwal.")
        for class_name, time in self.classes:
            print(f'- {class_name} pada {time}')

    def show_tasks(self):
        print("\n📝 Daftar Tugas:")
        if not self.tasks:
            print("Belum ada tugas.")
        for task in self.tasks:
            print(f'- {task}')

    def update_task_status(self, task_name, new_status):
        for task in self.tasks:
            if task.name == task_name:
                task.update_status(new_status)
                print(f"✅ Status '{task_name}' diperbarui menjadi '{new_status}'")
                return
        print("⚠️ Tugas tidak ditemukan!")

# Fungsi utama (interaktif)
def main():
    schedule = Schedule()

    while True:
        print("\n📌 MENU:")
        print("1. Tambah Jadwal Kuliah")
        print("2. Tambah Tugas")
        print("3. Lihat Jadwal Kuliah")
        print("4. Lihat Tugas")
        print("5. Ubah Status Tugas")
        print("0. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            nama = input("Nama Mata Kuliah: ")
            waktu = input("Hari & Jam (misal: Senin 08:00): ")
            schedule.add_class(nama, waktu)
            print("✅ Jadwal ditambahkan.")
        
        elif choice == "2":
            nama = input("Nama Tugas: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            tugas = Task(nama, deadline)
            schedule.add_task(tugas)
            print("✅ Tugas ditambahkan.")
        
        elif choice == "3":
            schedule.show_schedule()

        elif choice == "4":
            schedule.show_tasks()

        elif choice == "5":
            nama = input("Masukkan nama tugas yang ingin diubah: ")
            status = input("Status baru (Pending/In Progress/Completed): ")
            schedule.update_task_status(nama, status)

        elif choice == "0":
            print("👋 Keluar dari program.")
            break

        else:
            print("⚠️ Pilihan tidak valid!")

# Jalankan
if __name__ == "__main__":
    main()
