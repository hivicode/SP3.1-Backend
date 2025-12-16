# CRUD Flask MySQL dengan Upload File

Aplikasi CRUD dengan fitur upload gambar produk menggunakan Flask dan MySQL.

## Deskripsi

Aplikasi web untuk mengelola data produk UMKM dengan upload foto produk.

## Setup Database

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
app.config['MYSQL_DB'] = 'crud_upload_db'
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses di browser: http://127.0.0.1:5000

## Fitur

- Lihat daftar produk dengan foto
- Tambah produk dengan upload foto
- Edit produk dan ganti foto
- Hapus produk beserta fotonya

## Format File yang Diizinkan

- JPG/JPEG
- PNG
- GIF

## Struktur Folder

```
crud-flask-mysql-upload/
├── app.py
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
└── uploads/
    └── (file gambar tersimpan di sini)
```

