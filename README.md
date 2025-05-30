

 2. Strategy Pattern – StatusStrategy
Memisahkan logika penentuan status tugas berdasarkan progress.

python

class StatusStrategy:
    def get_status(self, progress): pass

class DefaultStatusStrategy(StatusStrategy):
    def get_status(self, progress):
        if progress == 0: return "Not Started"
        elif progress < 100: return "In Progress"
        else: return "Completed"
Digunakan di class Task:

python

class Task:
    def __init__(..., status_strategy=None):
        ...
        self.status_strategy = status_strategy or DefaultStatusStrategy()
        self.status = self.status_strategy.get_status(progress)

