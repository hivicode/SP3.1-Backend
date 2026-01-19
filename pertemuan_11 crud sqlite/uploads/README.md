# Uploads Folder

Folder ini digunakan untuk menyimpan file foto rumah yang diupload melalui aplikasi CRUD dengan SQLite.

## 📁 Deskripsi

Folder `uploads/` menyimpan semua file foto rumah yang diupload oleh user saat:
- Menambah data rumah baru
- Mengedit data rumah dan mengganti foto

## 📤 Format File yang Diizinkan

- JPG/JPEG
- PNG
- GIF

## 🔒 Keamanan

- File disimpan dengan nama yang aman menggunakan `secure_filename()` dari Werkzeug
- Validasi ekstensi file dilakukan sebelum upload
- File yang diupload tidak boleh melebihi ukuran tertentu (sesuai konfigurasi)

## 📝 Catatan

- Folder ini akan dibuat otomatis jika belum ada saat aplikasi pertama kali dijalankan
- File lama akan dihapus saat data dihapus atau foto diganti
- Jangan hapus file secara manual kecuali yakin file tersebut tidak digunakan lagi

## 🗑️ Cleanup

Untuk membersihkan file yang tidak terpakai, pastikan file tersebut tidak direferensikan di database sebelum menghapusnya.
