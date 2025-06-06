import unittest
import datetime
from ToDo.models import TodoItem, TaskFSM
from ToDo.storage import Storage
from ToDo.commands import CompleteTaskCommand, ExpireTaskCommand
from ToDo.config import Config
from ToDo.controller import (
    validate_title, validate_deadline,
    handle_create_task, handle_complete_task, handle_check_deadlines
)
#from ToDo.factory import TaskFactory

class TestTodoItem(unittest.TestCase):
    def setUp(self):
        self.title = "Test Task"
        self.deadline = "2025-12-31 23:59"
        self.task = TodoItem(self.title, self.deadline)

    def test_initial_state(self):
        self.assertEqual(self.task.title, self.title)
        self.assertEqual(self.task.status, "Created")
        self.assertEqual(self.task.deadline.strftime(Config().time_format), self.deadline)

    def test_complete_transition(self):
        self.task.complete()
        self.assertEqual(self.task.status, "Completed")

    def test_expire_transition(self):
        self.task.expire()
        self.assertEqual(self.task.status, "Expired")


class TestStorage(unittest.TestCase):
    def setUp(self):
        Storage._todo_list.clear()
        self.task1 = TodoItem("A", "2025-12-01 10:00")
        self.task2 = TodoItem("B", "2025-12-02 10:00")
        self.task2.complete()
        Storage.add_task(self.task1)
        Storage.add_task(self.task2)

    def test_get_all(self):
        self.assertEqual(len(Storage.get_all()), 2)

    def test_get_active(self):
        active = Storage.get_active()
        self.assertEqual(len(active), 1)
        self.assertEqual(active[0].title, "A")

    def test_get_history(self):
        history = Storage.get_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].title, "B")


class TestCommands(unittest.TestCase):
    def test_complete_command(self):
        task = TodoItem("Command Test", "2025-12-31 23:59")
        cmd = CompleteTaskCommand(task)
        cmd.execute()
        self.assertEqual(task.status, "Completed")

    def test_expire_command(self):
        task = TodoItem("Command Test", "2025-12-31 23:59")
        cmd = ExpireTaskCommand(task)
        cmd.execute()
        self.assertEqual(task.status, "Expired")


class TestConfigSingleton(unittest.TestCase):
    def test_singleton(self):
        c1 = Config()
        c2 = Config()
        self.assertIs(c1, c2)
        self.assertEqual(c1.time_format, "%Y-%m-%d %H:%M")


class TestControllerValidation(unittest.TestCase):
    def test_validate_title_success(self):
        self.assertEqual(validate_title("  Halo  "), "Halo")

    def test_validate_title_fail_empty(self):
        with self.assertRaises(ValueError):
            validate_title("    ")

    def test_validate_title_fail_long(self):
        with self.assertRaises(ValueError):
            validate_title("x" * 101)

    def test_validate_deadline_success(self):
        d = "2025-01-01 12:00"
        self.assertEqual(validate_deadline(d).strftime(Config().time_format), d)

    def test_validate_deadline_fail(self):
        with self.assertRaises(ValueError):
            validate_deadline("invalid-date")


class TestControllerHandlers(unittest.TestCase):
    def setUp(self):
        Storage._todo_list.clear()

    def test_handle_create_task(self):
        task = handle_create_task("My Task", "2025-12-01 10:00")
        self.assertEqual(task.title, "My Task")
        self.assertEqual(len(Storage.get_all()), 1)

    def test_handle_create_task_limit(self):
        for i in range(Config().max_tasks):
            handle_create_task(f"Task{i}", "2025-12-01 10:00")
        with self.assertRaises(Exception):
            handle_create_task("One more", "2025-12-01 10:00")

    def test_handle_complete_task(self):
        handle_create_task("To Complete", "2025-12-01 10:00")
        task = handle_complete_task(0)
        self.assertEqual(task.status, "Completed")

    def test_handle_complete_task_invalid_index(self):
        with self.assertRaises(ValueError):
            handle_complete_task(0)
        handle_create_task("Test", "2025-12-01 10:00")
        with self.assertRaises(IndexError):
            handle_complete_task(10)

    def test_handle_check_deadlines(self):
        past_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(Config().time_format)
        handle_create_task("Old Task", past_time)
        expired = handle_check_deadlines()
        self.assertEqual(len(expired), 1)
        self.assertEqual(expired[0].status, "Expired")


# class TestFactory(unittest.TestCase):
#     def test_create_task(self):
#         task = TaskFactory.create_task("Hello", "2025-12-01 10:00")
#         self.assertIsInstance(task, TodoItem)
#         self.assertEqual(task.title, "Hello")

if __name__ == '__main__':
    unittest.main()