from ToDoList import (
    create_task,
    get_active_tasks,
    get_history_tasks,
    complete_task_by_index,
    check_deadlines,
    config
)
import datetime


def tampilkan_menu():
    """
    Menampilkan menu utama dan menangani interaksi pengguna.
    """
    print("📝 Aplikasi To-Do List FSM (Refactored)\n")

    while True:
        print("Menu:")
        print("1. Tambah task")
        print("2. Lihat semua task aktif")
        print("3. Tandai task selesai")
        print("4. Cek deadline")
        print("5. Lihat riwayat tugas")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-5): ")

        try:
            if pilihan == '1':
                # Tambah task baru
                judul = input("Judul tugas: ")
                deadline = input(f"Deadline (format: {config.time_format}): ")
                create_task(judul, deadline)
                print("✅ Task berhasil ditambahkan!\n")

            elif pilihan == '2':
                # Lihat semua task aktif
                daftar_aktif = get_active_tasks()
                if not daftar_aktif:
                    print("📭 Tidak ada tugas aktif.\n")
                else:
                    print("\n📋 Tugas Aktif:")
                    for i, task in enumerate(daftar_aktif, start=1):
                        print(f"{i}. {task}")
                    print()

            elif pilihan == '3':
                # Tandai task sebagai selesai
                daftar_aktif = get_active_tasks()
                if not daftar_aktif:
                    print("🚫 Tidak ada task yang bisa diselesaikan.\n")
                    continue

                print("\n✅ Daftar Tugas Aktif:")
                for i, task in enumerate(daftar_aktif, start=1):
                    print(f"{i}. {task}")

                idx_input = input("Masukkan nomor task: ")
                idx = int(idx_input) - 1
                complete_task_by_index(idx)
                print("✅ Task ditandai selesai!\n")

            elif pilihan == '4':
                # Cek dan tandai task yang melewati deadline
                tugas_kedaluwarsa = check_deadlines()
                if not tugas_kedaluwarsa:
                    print("⏰ Tidak ada task yang expired.\n")
                else:
                    print("\n⚠️ Task yang sudah lewat deadline:")
                    for task in tugas_kedaluwarsa:
                        print(f"😱 Task '{task.title}' telah lewat deadline.")
                    print()

            elif pilihan == '5':
                # Tampilkan riwayat tugas yang telah selesai atau kedaluwarsa
                riwayat = get_history_tasks()
                if not riwayat:
                    print("📦 Belum ada riwayat tugas.\n")
                else:
                    print("\n📜 Riwayat Tugas:")
                    for i, task in enumerate(riwayat, start=1):
                        print(f"{i}. {task}")
                    print()

            elif pilihan == '0':
                # Keluar dari aplikasi
                print("👋 Keluar dari program.")
                break

            else:
                print("⚠️ Menu tidak valid.\n")

        except Exception as error:
            print(f"⚠️ Terjadi kesalahan: {error}\n")


if __name__ == '__main__':
    tampilkan_menu()
