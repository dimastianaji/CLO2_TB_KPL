import unittest
from datetime import datetime, timedelta
from ToDoList import (
    TodoItem,
    config,
    create_task,
    get_active_tasks,
    get_history_tasks,
    complete_task_by_index,
    check_deadlines,
    todo_list
)

class TestToDoList(unittest.TestCase):
    def setUp(self):
        # Bersihkan daftar tugas sebelum setiap pengujian
        todo_list.clear()
        self.future_time = (datetime.now() + timedelta(days=1)).strftime(config.time_format)
        self.past_time = (datetime.now() - timedelta(days=1)).strftime(config.time_format)

    def test_create_valid_task(self):
        # Test membuat task valid
        task = create_task("Tugas 1", self.future_time)
        self.assertEqual(task.title, "Tugas 1")
        self.assertEqual(task.status, "Created")
        self.assertEqual(len(todo_list), 1)

    def test_create_task_exceeds_limit(self):
        # Test batas maksimal task
        config.max_tasks = 2
        create_task("Tugas 1", self.future_time)
        create_task("Tugas 2", self.future_time)
        with self.assertRaises(Exception) as error:
            create_task("Tugas 3", self.future_time)
        self.assertIn("Maksimum jumlah task tercapai", str(error.exception))

    def test_create_task_exactly_max_limit(self):
        # Test saat task mencapai batas maksimum tapi tidak melebihi
        config.max_tasks = 3
        create_task("T1", self.future_time)
        create_task("T2", self.future_time)
        create_task("T3", self.future_time)
        self.assertEqual(len(todo_list), 3)

    def test_invalid_date_format(self):
        # Test input format tanggal yang salah
        with self.assertRaises(ValueError):
            TodoItem("Salah Format", "31-12-2024")

    def test_complete_task(self):
        # Test menyelesaikan task
        create_task("Selesai", self.future_time)
        task = complete_task_by_index(0)
        self.assertEqual(task.status, "Completed")

    def test_complete_task_invalid_index(self):
        # Test menyelesaikan task dengan indeks tidak valid
        with self.assertRaises(IndexError):
            complete_task_by_index(0)

    def test_get_active_tasks(self):
        # Test pengambilan task yang masih aktif
        create_task("Aktif 1", self.future_time)
        create_task("Aktif 2", self.future_time)
        self.assertEqual(len(get_active_tasks()), 2)

    def test_get_history_tasks(self):
        # Test pengambilan task yang sudah selesai atau expired
        task = create_task("Riwayat", self.past_time)
        task.expire()
        history = get_history_tasks()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0].status, "Expired")

    def test_check_deadlines(self):
        # Test fungsi pengecekan deadline
        task_expired = create_task("Kadaluarsa", self.past_time)
        task_active = create_task("Aman", self.future_time)
        expired = check_deadlines(now=datetime.now())
        self.assertIn(task_expired, expired)
        self.assertNotIn(task_active, expired)
        self.assertEqual(task_expired.status, "Expired")
        self.assertEqual(task_active.status, "Created")

    def test_check_deadlines_custom_now(self):
        # Test pengecekan deadline dengan waktu simulasi
        deadline = (datetime.now() + timedelta(minutes=1)).strftime(config.time_format)
        task = create_task("Simulasi", deadline)
        future_now = datetime.now() + timedelta(minutes=2)
        expired = check_deadlines(now=future_now)
        self.assertIn(task, expired)
        self.assertEqual(task.status, "Expired")

    def test_check_deadlines_no_expired(self):
        # Test ketika tidak ada task yang kadaluarsa
        task = create_task("Belum Kadaluarsa", self.future_time)
        expired = check_deadlines()
        self.assertEqual(len(expired), 0)
        self.assertEqual(task.status, "Created")

    def test_todoitem_str_representation(self):
        # Test format string dari objek TodoItem
        task = create_task("Tugas String", self.future_time)
        expected = f"Tugas String | Created | Due: {task.deadline.strftime(config.time_format)}"
        self.assertEqual(str(task), expected)

    def test_taskfsm_state_transitions(self):
        # Test transisi status task dengan FSM manual
        task = TodoItem("FSM 1", self.future_time)
        self.assertEqual(task.status, "Created")
        task.fsm.set_completed()
        self.assertEqual(task.status, "Completed")

        task2 = TodoItem("FSM 2", self.future_time)
        task2.fsm.set_expired()
        self.assertEqual(task2.status, "Expired")


if __name__ == '__main__':
    unittest.main()