import unittest
from task_manager import Task, TaskManager

class TestTask(unittest.TestCase):
    def test_status_update(self):
        task = Task("Unit Test", "2025-12-31", 0)
        self.assertEqual(task.status, "Not Started")
        task.update_progress(40)
        self.assertEqual(task.status, "In Progress")
        task.update_progress(100)
        self.assertEqual(task.status, "Completed")

    def test_late_task(self):
        task = Task("Tugas Lama", "2000-01-01", 50)
        self.assertTrue(task.is_late())

class TestTaskManager(unittest.TestCase):
    def test_add_remove_task(self):
        manager = TaskManager()
        task = Task("Tes Tambah", "2025-12-31")
        manager.add_task(task)
        self.assertEqual(len(manager.tasks), 1)
        manager.remove_task("Tes Tambah")
        self.assertEqual(len(manager.tasks), 0)

if __name__ == "__main__":
    unittest.main()
