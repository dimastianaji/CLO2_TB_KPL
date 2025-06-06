from controller import (
    handle_create_task, handle_complete_task,
    handle_check_deadlines
)
from ToDo.storage import get_active_tasks, get_history_tasks
from ToDo.config import Config
from ToDo.view import print_menu, print_tasks

config = Config()

def main():
    while True:
        print_menu()
        pilihan = input("Pilih menu (0-5): ")

        try:
            if pilihan == '1':
                title = input("Judul: ")
                deadline = input(f"Deadline ({config.time_format}): ")
                handle_create_task(title, deadline)
                print("✅ Task berhasil ditambahkan!\n")

            elif pilihan == '2':
                print_tasks(get_active_tasks(), "📋 Tugas Aktif:")

            elif pilihan == '3':
                tasks = get_active_tasks()
                print_tasks(tasks, "✅ Pilih tugas untuk ditandai selesai:")
                if not tasks:
                    continue
                index = int(input("Masukkan nomor: ")) - 1
                handle_complete_task(index)
                print("✅ Task ditandai selesai!\n")

            elif pilihan == '4':
                expired = handle_check_deadlines()
                if not expired:
                    print("⏰ Tidak ada task expired.\n")
                else:
                    print("⚠️ Task yang lewat deadline:")
                    for t in expired:
                        print(f"😱 {t.title}")
                    print()

            elif pilihan == '5':
                print_tasks(get_history_tasks(), "📜 Riwayat Tugas:")

            elif pilihan == '0':
                print("👋 Keluar dari aplikasi.")
                break

            else:
                print("⚠️ Menu tidak valid.\n")

        except Exception as e:
            print(f"⚠️ Terjadi kesalahan: {e}\n")

if __name__ == '__main__':
    main()
