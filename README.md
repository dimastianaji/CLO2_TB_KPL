 Fitur dan Penerapan Prinsip Pemrograman
 1. Code Reuse (Pemanfaatan Kode Ulang)
Program ini menerapkan code reuse melalui pemisahan logika ke dalam method dan class yang modular:

Method determine_status() dan is_late() pada class Task digunakan ulang oleh beberapa bagian kode seperti update_progress() dan pengecekan status tugas di TaskManager.

Class TaskManager menggunakan kembali method milik Task untuk operasi manajemen tugas, seperti:

update_progress() dipanggil ulang saat memperbarui progres tugas.

is_late() digunakan untuk menyeleksi tugas yang melewati deadline.

Format penampilan data tugas (__str__) diatur dalam satu tempat sehingga semua tampilan konsisten.

⚙️ 2. Parameterization (Pengaturan Nilai Lewat Parameter)
Program menghindari hardcoding dengan penggunaan parameter:

Deadline tugas ditentukan melalui parameter deadline_str pada class Task.

Progress awal tugas juga bisa diatur lewat parameter default progress=0.

Format tanggal diatur secara global melalui objek config, bukan ditulis langsung dalam logika parsing.

Keuntungan:

Memudahkan pengujian dan perubahan tanpa mengedit seluruh kode.

Memberi fleksibilitas dalam membuat tugas dengan berbagai konfigurasi.

 3. Generic (Generik / Tipe Umum)
Saat ini, kode belum sepenuhnya menerapkan tipe generik, tetapi dapat dikembangkan untuk mendukungnya, terutama jika ingin membuat manajer tugas lebih fleksibel terhadap tipe objek lain (misalnya Event, Reminder, dll).

Contoh Implementasi Generik (Menggunakan Python typing.Generic)
python
Salin
Edit
from typing import TypeVar, Generic, List

T = TypeVar('T')  # Tipe generik

class Manager(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def add(self, item: T):
        self.items.append(item)

    def remove(self, item: T):
        self.items.remove(item)

    def get_all(self) -> List[T]:
        return self.items
Dengan itu, kita bisa membuat manajer tugas generik:

python
Salin
Edit
task_manager = Manager[Task]()
task_manager.add(Task("Tugas 1", "2025-05-05"))
Manfaat:

Generik ini memungkinkan manajemen berbagai jenis objek selain Task, tanpa membuat ulang class baru.

Meningkatkan fleksibilitas dan reusability sistem.

Rangkuman
Prinsip	Penerapan
Code Reuse	Method dan class reusable, pemisahan logika
Parameterization	Nilai seperti deadline, progress, dan format tanggal bisa dikonfigurasi
Generic	Dapat diterapkan melalui Generic[T] untuk membuat manajer tugas fleksibel