# Pertemuan 6 - CRUD Flask MySQL dengan Upload File

## Setup Database

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

## Install Dependencies

```bash
pip install flask flask-mysqldb
```

## Konfigurasi

Edit file `app.py` sesuai dengan konfigurasi MySQL Anda:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crud_upload_db'
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses aplikasi di browser: `http://127.0.0.1:5000`

## Fitur

- Tambah produk dengan upload gambar
- Edit produk dan update gambar
- Hapus produk beserta gambar
- Menampilkan daftar produk dengan gambar

## Format File yang Diizinkan

- JPG/JPEG
- PNG
- GIF

