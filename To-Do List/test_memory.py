from memory_profiler import profile
from ToDo.controller import handle_create_task
from ToDo.config import Config

@profile
def test_memory():
    config = Config()
    config.max_tasks = 10  
    for i in range(10):
        handle_create_task(f"Task {i}", "2025-12-31 23:59")

if __name__ == '__main__':
    test_memory()
