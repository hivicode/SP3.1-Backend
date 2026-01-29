# Pertemuan 6 - CRUD Flask MySQL dengan Upload File

Aplikasi CRUD lengkap dengan fitur upload file gambar menggunakan Flask dan MySQL.

## ?? Deskripsi

Pertemuan ini membahas implementasi operasi CRUD (Create, Read, Update, Delete) dengan fitur upload file gambar. Aplikasi mengelola data stok produk dengan kemampuan untuk mengupload dan menampilkan gambar produk.

## ?? Fitur Utama

- **CRUD Lengkap**: Create, Read, Update, Delete data stok
- **Upload Gambar**: Upload dan kelola gambar produk
- **Display Gambar**: Menampilkan gambar produk di daftar dan detail
- **File Management**: Hapus file gambar saat data dihapus
- **Responsive Design**: Desain responsif menggunakan Bootstrap

## ?? Setup Database

Buat database dan tabel dengan menjalankan SQL berikut:

```sql
CREATE DATABASE crud_upload_db;

USE crud_upload_db;

CREATE TABLE stok (
    kode VARCHAR(50) PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    harga INT NOT NULL,
    filename VARCHAR(255)
);
```

## ?? Install Dependencies

```bash
pip install flask flask-mysqldb werkzeug
```

##  Konfigurasi

Edit file `app.py` sesuai dengan konfigurasi MySQL Anda:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'  # Ganti dengan password MySQL Anda
app.config['MYSQL_DB'] = 'crud_upload_db'
```

## ?? Menjalankan Aplikasi

```bash
cd crud-flask-mysql-upload
python app.py
```

Akses aplikasi di browser: `http://127.0.0.1:5000`

## ?? Struktur Folder

```
pertemuan_06/
+-- README.md
+-- crud-flask-mysql-upload/
    +-- app.py
    +-- README.md
    +-- templates/
       +-- index.html
       +-- add.html
       +-- edit.html
    +-- uploads/
        +-- (file gambar tersimpan di sini)
```

## ?? Fitur yang Dipelajari

 Upload file dengan Flask  
 Validasi ekstensi file  
 Penyimpanan file dengan `secure_filename()`  
 Menampilkan gambar dari folder uploads  
 Menghapus file saat data dihapus  
 Form dengan `enctype="multipart/form-data"`  
 File handling dengan Werkzeug  

## ?? Format File yang Diizinkan

- JPG/JPEG
- PNG
- GIF

## ?? Cara Menggunakan

1. **Tambah Data Baru**
   - Klik tombol "Tambah Data"
   - Isi form (kode, nama, harga)
   - Pilih file gambar
   - Submit form

2. **Edit Data**
   - Klik tombol "Edit" pada data yang ingin diubah
   - Update data dan/atau ganti gambar
   - Submit form

3. **Hapus Data**
   - Klik tombol "Hapus" pada data yang ingin dihapus
   - Data dan file gambar akan dihapus

## ?? Teknologi

- **Flask** - Web framework
- **Flask-MySQLdb** - MySQL connector
- **Werkzeug** - File upload handling
- **Bootstrap** - CSS framework
- **Jinja2** - Template engine

## ?? Catatan Penting

- Folder `uploads/` akan dibuat otomatis jika belum ada
- File disimpan dengan nama yang aman menggunakan `secure_filename()`
- File lama akan dihapus saat data dihapus atau gambar diganti
- Pastikan folder `uploads/` memiliki permission write

## ?? Tujuan Pembelajaran

1. Memahami cara upload file dengan Flask
2. Implementasi validasi file upload
3. Menyimpan dan mengelola file upload
4. Menampilkan gambar dari folder static/uploads
5. Menghapus file saat data dihapus
6. Form handling dengan multipart/form-data

## ?? Keamanan

-  Validasi ekstensi file
-  Menggunakan `secure_filename()` untuk mencegah path traversal
-  Untuk production, tambahkan validasi ukuran file
-  Untuk production, tambahkan validasi content file (bukan hanya ekstensi)
