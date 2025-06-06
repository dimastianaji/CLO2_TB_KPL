import unittest
import datetime
from ToDo.commands import CompleteTaskCommand, ExpireTaskCommand
from ToDo.controller import (
    handle_create_task,
    handle_complete_task,
    handle_check_deadlines
)
from ToDo.storage import todo_list, get_all_tasks, get_active_tasks, get_history_tasks

class TestTodoList(unittest.TestCase):

    def setUp(self):
        # Reset todo_list setiap kali sebelum tes
        todo_list.clear()

    def test_create_task(self):
        task = handle_create_task("Belajar FSM", "2025-06-07 10:00")
        self.assertEqual(task.title, "Belajar FSM")
        self.assertEqual(task.status, "Created")
        self.assertEqual(len(get_all_tasks()), 1)

    def test_complete_task_command(self):
        task = handle_create_task("Selesaikan tugas", "2025-06-08 10:00")
        cmd = CompleteTaskCommand(task)
        cmd.execute()
        self.assertEqual(task.status, "Completed")

    def test_expire_task_command(self):
        task = handle_create_task("Tugas kemarin", "2025-06-01 10:00")
        cmd = ExpireTaskCommand(task)
        cmd.execute()
        self.assertEqual(task.status, "Expired")

    def test_handle_complete_task(self):
        handle_create_task("Matikan alarm", "2025-06-08 09:00")
        active = get_active_tasks()
        result = handle_complete_task(0)
        self.assertEqual(result.status, "Completed")
        self.assertEqual(len(get_history_tasks()), 1)

    def test_handle_check_deadlines(self):
        handle_create_task("Tugas lewat", "2025-06-01 09:00")
        expired = handle_check_deadlines(now=datetime.datetime(2025, 6, 6, 10, 0))
        self.assertEqual(len(expired), 1)
        self.assertEqual(expired[0].status, "Expired")

    def test_max_task_limit(self):
        from ToDo.config import Config
        max_tasks = Config().max_tasks
        for i in range(max_tasks):
            handle_create_task(f"Tugas {i+1}", "2025-06-09 10:00")
        with self.assertRaises(Exception) as context:
            handle_create_task("Tugas ekstra", "2025-06-09 11:00")
        self.assertIn("Maksimum jumlah task", str(context.exception))

    def test_invalid_complete_index(self):
        handle_create_task("Tugas 1", "2025-06-09 10:00")
        with self.assertRaises(IndexError):
            handle_complete_task(5)

if __name__ == '__main__':
    unittest.main()
