
 1. Parameterization (Pengaturan nilai lewat parameter)
Artinya: nilai-nilai penting seperti deadline, progress, format tanggal, tidak ditulis langsung (hardcoded), tapi bisa diatur lewat parameter atau konfigurasi.

Contoh di kode :



class Task:
    def __init__(self, title, deadline_str, progress=0):  # ← parameterisasi judul, deadline, dan progress
        self.deadline = datetime.datetime.strptime(deadline_str, config.time_format)  # ← format tanggal pakai config



class Config:
    def __init__(self):
        self.time_format = "%Y-%m-%d"  # ← global setting, bukan ditulis ulang di setiap tempat
 
 Manfaatnya:

Mudah diubah saat testing atau konfigurasi lain.

Konsisten di seluruh aplikasi (misalnya format tanggal).

Lebih fleksibel untuk dikembangkan.

 2. Code Reuse (Pemanfaatan ulang kode)
Artinya: logika atau fungsi yang sama digunakan di banyak tempat, supaya tidak ditulis ulang.

Contoh reuse di dalam class Task:



def update_progress(self, new_progress):
    self.progress = new_progress
    self.status = self.determine_status()  # ← pakai ulang method determine_status()



def __str__(self):
    late_flag = " TERLAMBAT" if self.is_late() else ""  # ← pakai ulang method is_late()
Contoh reuse di dalam class TaskManager:




def update_task_progress(self, title, new_progress):
    for task in self.tasks:
        if task.title == title:
            task.update_progress(new_progress)  # ← pakai method bawaan Task
 
 Manfaatnya:

Kode lebih pendek dan rapi.

Mengurangi duplikasi.

Jika logika diubah, cukup ubah di satu tempat saja.

 3. Generic (Tipe Umum)
Artinya: membuat class atau fungsi yang bisa dipakai untuk tipe data apa pun, tidak hanya Task. Misalnya bisa dipakai untuk Event, Reminder, dll.

Contoh implementasi:

T = TypeVar('T')

class Manager(Generic[T]):
    def __init__(self):
        self.items: List[T] = []  # ← bisa menyimpan apa pun: Task, Event, dll
Lalu, kita bisa pakai seperti ini:


task_manager = Manager[Task]()
event_manager = Manager[Event]()  # ← manager ini bisa digunakan ulang untuk jenis data yang berbeda
 Manfaatnya:

Kode jadi lebih fleksibel dan reusable.

Tidak perlu bikin ulang class yang sama untuk setiap jenis data.





🔚 Kesimpulan Design Pattern yang Diterapkan
Design Pattern	Fungsi	Tempat Diterapkan
Singleton	Satu instance global untuk config	Config class
Strategy	Logika status yang bisa diganti-ganti	Task class (status logic)
Factory	Abstraksi penciptaan objek Task	TaskFactory class
(Optional) Observer	Reaksi terhadap perubahan progress/status	Bisa ditambahkan ke Task

 
