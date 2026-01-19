# Uploads Folder

Folder ini digunakan untuk menyimpan file gambar yang diupload melalui aplikasi CRUD.

## 📁 Deskripsi

Folder `uploads/` menyimpan semua file gambar yang diupload oleh user saat:
- Menambah data stok baru
- Mengedit data stok dan mengganti gambar

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
- File lama akan dihapus saat data dihapus atau gambar diganti
- Jangan hapus file secara manual kecuali yakin file tersebut tidak digunakan lagi

## 🗑️ Cleanup

Untuk membersihkan file yang tidak terpakai, pastikan file tersebut tidak direferensikan di database sebelum menghapusnya.
