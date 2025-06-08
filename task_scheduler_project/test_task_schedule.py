import unittest
from task_schedule import Task, Schedule

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Tugas A", "2025-06-10")
        self.assertEqual(task.name, "Tugas A")
        self.assertEqual(task.deadline, "2025-06-10")
        self.assertEqual(task.status, "Pending")

    def test_valid_status_update(self):
        task = Task("Tugas A", "2025-06-10")
        task.update_status("Completed")
        self.assertEqual(task.status, "Completed")

    def test_invalid_status_update(self):
        task = Task("Tugas A", "2025-06-10")
        task.update_status("Selesai")  # Tidak valid
        self.assertEqual(task.status, "Pending")  # Tidak berubah

class TestSchedule(unittest.TestCase):
    def test_add_class(self):
        schedule = Schedule()
        schedule.add_class("Matematika", "Senin 08:00")
        self.assertEqual(schedule.classes, [("Matematika", "Senin 08:00")])

    def test_add_task(self):
        schedule = Schedule()
        task = Task("Tugas A", "2025-06-10")
        schedule.add_task(task)
        self.assertIn(task, schedule.tasks)

    def test_update_task_status(self):
        schedule = Schedule()
        task = Task("Tugas A", "2025-06-10")
        schedule.add_task(task)
        schedule.update_task_status("Tugas A", "In Progress")
        self.assertEqual(task.status, "In Progress")

if __name__ == '__main__':
    unittest.main()
