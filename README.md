🔧 Design Pattern: Command Pattern
Tujuan:
Memisahkan logika perintah (seperti menampilkan tugas atau mengupdate progress) ke dalam objek-objek terpisah agar mudah dikelola, diperluas, dan diuji.

Penerapan:
Setiap menu seperti "Lihat Semua Tugas", "Update Progress Tugas", dan lainnya diwakili oleh kelas command:

PrintAllTasksCommand

PrintCompletedTasksCommand

PrintInProgressTasksCommand

UpdateProgressCommand

ExitCommand

Kelas MenuInvoker berfungsi mengeksekusi perintah berdasarkan input pengguna.

Keuntungan:

Kode lebih modular dan bersih.

Mudah menambah atau mengubah aksi menu tanpa menyentuh struktur utama program.

Cocok untuk sistem menu interaktif atau antarmuka pengguna.
