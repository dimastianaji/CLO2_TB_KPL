from ToDo.controller import (
    handle_create_task, handle_complete_task,
    handle_check_deadlines, validate_title, validate_deadline
)
from ToDo.task_storage import Storage
from ToDo.config import Config
from ToDo.view import print_menu, print_tasks

config = Config()

def safe_input(prompt, expected_type=int, allow_blank=False):
    while True:
        value = input(prompt)
        if allow_blank and value.strip() == "":
            return None
        try:
            return expected_type(value)
        except ValueError:
            print(f"⚠️ Masukkan harus bertipe {expected_type.__name__}.\n")

def main():
    while True:
        print_menu()
        pilihan = input("Pilih menu (0-5): ")

        try:
            if pilihan == '1':
                title = validate_title(input("Judul: "))
                deadline = input(f"Deadline ({config.time_format}): ")
                validate_deadline(deadline)
                handle_create_task(title, deadline)
                print("✅ Task berhasil ditambahkan!\n")

            elif pilihan == '2':
                print_tasks(Storage.get_active(), "📋 Tugas Aktif:")

            elif pilihan == '3':
                tasks = Storage.get_active()
                print_tasks(tasks, "✅ Pilih tugas untuk ditandai selesai:")
                if not tasks:
                    continue
                index = safe_input("Masukkan nomor: ", int) - 1
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
                print_tasks(Storage.get_history(), "📜 Riwayat Tugas:")

            elif pilihan == '0':
                print("👋 Keluar dari aplikasi.")
                break

            else:
                print("⚠️ Menu tidak valid.\n")

        except (ValueError, IndexError) as e:
            print(f"⚠️ Kesalahan input: {e}\n")
        except Exception as e:
            print("⚠️ Terjadi kesalahan internal.\n")

if __name__ == '__main__':
    main()
