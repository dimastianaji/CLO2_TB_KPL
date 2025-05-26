# 📝 To-Do List FSM (Design Pattern Edition)

A modular and extensible To-Do List CLI application written in Python.  
This project demonstrates how to implement core design patterns—**State**, **Factory**, and **Command**—in managing task state transitions using a **Finite State Machine (FSM)**.

---

## 🎯 Tujuan Proyek

Membangun aplikasi manajemen tugas yang bersih, terstruktur, dan mudah dikembangkan menggunakan prinsip OOP dan *design pattern*. Aplikasi ini cocok sebagai bahan pembelajaran arsitektur perangkat lunak serta pengelolaan status objek secara dinamis.

---

## 🚀 Fitur Utama

- ✅ Tambah tugas dengan tenggat waktu
- 📋 Lihat daftar tugas aktif
- ✔️ Tandai tugas sebagai selesai
- ⏰ Tandai otomatis sebagai *expired* jika melewati tenggat
- 📜 Lihat riwayat tugas (Completed & Expired)
- 🧩 Struktur modular dengan design pattern

---

## 🧠 Design Pattern yang Digunakan

| Design Pattern       | Fungsi                                                                 |
|----------------------|------------------------------------------------------------------------|
| **State Pattern**     | Mengatur status task dengan FSM: Created → Completed / Expired        |
| **Factory Pattern**   | Memisahkan logika pembuatan task dari kode utama                      |
| **Command Pattern**   | Membungkus aksi `complete` dan `expire` sebagai objek mandiri         |
| **MVC-like Structure**| Pemisahan kode menjadi model, view, controller, dan penyimpanan       |
| **Configuration Object** | Menyimpan semua konfigurasi runtime secara terpusat              |

---

## 🗂️ Struktur Proyek
todo_app/
├── main.py # Entry-point CLI
├── config.py # Konfigurasi aplikasi
├── models.py # TodoItem & FSM (State Pattern)
├── factory.py # TaskFactory (Factory Pattern)
├── commands.py # Command classes (Command Pattern)
├── controller.py # Logika bisnis aplikasi
├── storage.py # Penyimpanan sementara (in-memory)
└── view.py # Antarmuka pengguna berbasis teks


---
## 📷 Cuplikan Menu
📝 Aplikasi To-Do List FSM (Design Pattern)

1. Tambah task
2. Lihat semua task aktif
3. Tandai task selesai
4. Cek deadline
5. Lihat riwayat tugas
0. Keluar

