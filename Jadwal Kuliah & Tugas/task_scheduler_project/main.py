# main.py

from task_schedule import Task, Schedule

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

if __name__ == "__main__":
    main()
