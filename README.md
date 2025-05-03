#  Program Manajemen Tugas Harian Mahasiswa

##  Fitur
- Tambah tugas dengan judul, deadline, dan progress.
- Status otomatis: 
  - Not Started (0%)
  - In Progress (1–99%)
  - Completed (100%)
- Update progress tugas.
- Deteksi otomatis jika tugas sudah melewati deadline.
- Cetak daftar tugas dengan status dan tanda "TERLAMBAT" jika perlu.

##  Teknik Pemrograman

###  Parameterisasi
- Format tanggal (`%Y-%m-%d`) dan fitur auto-update status bisa diatur dari class `Config`.
- Tugas dibuat dengan parameter bebas (judul, deadline, progress).

###  Code Reuse
- Fungsi `determine_status()` dan `print_task_list()` digunakan di banyak tempat untuk efisiensi dan menghindari duplikasi kode.

###  Generalisasi
- Class `Task` dibuat fleksibel dan bisa digunakan untuk jenis tugas apapun, tidak terbatas pada tugas kuliah saja.
