import unittest
from main import Task, Schedule  # Mengimpor dari main.py

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Tugas 1", "2025-06-01")
        self.assertEqual(task.name, "Tugas 1")
        self.assertEqual(task.deadline, "2025-06-01")
        self.assertEqual(task.status, "Pending")

    def test_update_status_valid(self):
        task = Task("Tugas 2", "2025-06-02")
        task.update_status("In Progress")
        self.assertEqual(task.status, "In Progress")

    def test_update_status_invalid(self):
        task = Task("Tugas 3", "2025-06-03")
        task.update_status("Selesai")  # Status tidak valid
        self.assertEqual(task.status, "Pending")

class TestSchedule(unittest.TestCase):
    def test_add_class(self):
        sched = Schedule()
        sched.add_class("Matematika", "Senin 09:00")
        self.assertIn(("Matematika", "Senin 09:00"), sched.classes)

    def test_add_task(self):
        sched = Schedule()
        task = Task("Tugas 4", "2025-06-04")
        sched.add_task(task)
        self.assertIn(task, sched.tasks)

    def test_update_task_status_found(self):
        sched = Schedule()
        task = Task("Tugas 5", "2025-06-05")
        sched.add_task(task)
        sched.update_task_status("Tugas 5", "Completed")
        self.assertEqual(task.status, "Completed")

    def test_update_task_status_not_found(self):
        sched = Schedule()
        task = Task("Tugas 6", "2025-06-06")
        sched.add_task(task)
        sched.update_task_status("Tugas Lain", "Completed")
        self.assertEqual(task.status, "Pending")

if __name__ == "__main__":
    unittest.main()
