# CRUD Flask dengan Search dan Pagination

Aplikasi CRUD dengan fitur pencarian dan pagination menggunakan Flask dan MySQL.

## Deskripsi

Aplikasi web untuk menampilkan data produk UMKM dengan fitur pencarian berdasarkan nama barang dan pagination untuk membagi data menjadi beberapa halaman.

## Setup Database

```sql
CREATE DATABASE crud_db;
USE crud_db;

CREATE TABLE stok (
    kode VARCHAR(50) PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    harga INT NOT NULL
);
```


## Instalasi

```bash
pip install flask flask-mysqldb
```

## Konfigurasi

Edit konfigurasi MySQL di `app.py`:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crud_db'
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses di browser: http://127.0.0.1:5000

## Fitur

- Lihat daftar produk dengan pagination (5 item per halaman)
- Pencarian produk berdasarkan nama barang
- Navigasi halaman dengan tombol Previous dan Next
- Pencarian tetap aktif saat berpindah halaman
- Desain responsif dengan Bootstrap 5.3.0

## Struktur Folder

```
crud-flask-search-pagination/
├── app.py
└── templates/
    └── index.html
```

## Teknologi yang Digunakan

- Flask - Web framework
- Flask-MySQLdb - MySQL connector
- Bootstrap 5.3.0 - CSS framework
- Jinja2 - Template engine

