def print_menu():
    print("📝 Aplikasi To-Do List FSM (Design Pattern)\n")
    print("1. Tambah task")
    print("2. Lihat semua task aktif")
    print("3. Tandai task selesai")
    print("4. Cek deadline")
    print("5. Lihat riwayat tugas")
    print("0. Keluar")

def print_tasks(tasks, header):
    if not tasks:
        print("📭 Tidak ada tugas.\n")
    else:
        print(f"\n{header}")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()
