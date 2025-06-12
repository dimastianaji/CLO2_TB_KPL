# performance_test.py

import timeit

setup = '''
from task_schedule import Task, Schedule
s = Schedule()
for i in range(1000):
    s.add_task(Task(f"Tugas {i}", "2025-06-10"))
'''

test_code = '''
s.update_task_status("Tugas 1", "Completed")
'''

print("Waktu eksekusi:")
print(timeit.timeit(stmt=test_code, setup=setup, number=100))
