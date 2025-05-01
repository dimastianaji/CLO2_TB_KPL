from config import time_format, max_tasks
from task_fsm import buat_fsm
import datetime

todo_list = []

# Tambah task
print("📝 Tambah Task")
if len(todo_list) < max_tasks:
    title = input("Judul: ")
    deadline_str = input(f"Deadline ({time_format}): ")
    deadline = datetime.datetime.strptime(deadline_str, time_format)

    task = type('TodoItem', (), {})()
    task.title = title
    task.deadline = deadline
    task.status = 'Created'
    task.fsm = buat_fsm(task)

    todo_list.append(task)
    print("✅ Task ditambahkan.")
else:
    print("❌ Sudah penuh.")

# Lihat task
print("\n📋 Task Aktif:")
for i, t in enumerate(todo_list):
    if t.status == 'Created':
        print(f"{i+1}. {t.title} | {t.status} | Due: {t.deadline.strftime(time_format)}")

# Tandai selesai
idx = int(input("\nTask yang diselesaikan (nomor): ")) - 1
todo_list[idx].complete()
print(f"🎉 Task '{todo_list[idx].title}' selesai.")

# Cek deadline
print("\n⏰ Cek Expired:")
sekarang = datetime.datetime.now()
for task in todo_list:
    if task.status == 'Created' and sekarang > task.deadline:
        task.expire()
        print(f"💀 '{task.title}' expired.")

# Riwayat
print("\n📜 Riwayat:")
for task in todo_list:
    if task.status in ['Completed', 'Expired']:
        print(f"- {task.title} | {task.status}")
