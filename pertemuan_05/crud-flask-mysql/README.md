# CRUD Flask MySQL

Aplikasi CRUD sederhana menggunakan Flask dan MySQL.

## Deskripsi

Aplikasi web untuk mengelola data stok barang dengan operasi Create, Read, Update, dan Delete.

## Setup Database

```sql
CREATE DATABASE crud_db;
USE crud_db;

CREATE TABLE stok (
  kode VARCHAR(20) PRIMARY KEY,
  nama VARCHAR(100) NOT NULL,
  harga DECIMAL(10,2) NOT NULL,
  stok INT NOT NULL
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

- Lihat daftar stok barang
- Tambah data stok baru
- Edit data stok
- Hapus data stok

