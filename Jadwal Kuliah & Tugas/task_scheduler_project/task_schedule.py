class Task:
    VALID_STATUSES = {'Pending', 'In Progress', 'Completed'}

    def __init__(self, name, deadline):
        self.name = name.strip()
        self.deadline = deadline.strip()
        self.status = 'Pending'

    def update_status(self, new_status):
        if new_status in self.VALID_STATUSES:
            self.status = new_status
        else:
            print("⚠️ Status tidak valid!")

    def __str__(self):
        return f'Task: {self.name}, Deadline: {self.deadline}, Status: {self.status}'


class Schedule:
    def __init__(self):
        self.classes = []
        self.tasks = []

    def add_class(self, class_name, time):
        self.classes.append((class_name.strip(), time.strip()))

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
