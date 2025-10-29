# Pertemuan 7 - CRUD Flask dengan Search dan Pagination

## Deskripsi

Pertemuan ini membahas implementasi fitur pencarian dan pagination pada aplikasi CRUD Flask dengan MySQL.

## Setup Database

Buat database dan tabel dengan menjalankan SQL berikut:

```sql
CREATE DATABASE crud_upload_db;

USE crud_upload_db;

CREATE TABLE stok (
    kode VARCHAR(50) PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    harga INT NOT NULL
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
app.config['MYSQL_PASSWORD'] = 'root' ganti dengan password anda
app.config['MYSQL_DB'] = 'crud_upload_db'
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses aplikasi di browser: `http://127.0.0.1:5000`

## Fitur

- Pencarian produk berdasarkan nama barang
- Pagination dengan 5 item per halaman
- Navigasi halaman dengan tombol Previous dan Next
- Tampilan data dengan table Bootstrap
- Pencarian tetap aktif saat berpindah halaman

## Teknologi

- Flask
- Flask-MySQLdb
- Bootstrap 5.3.0
- Jinja2

