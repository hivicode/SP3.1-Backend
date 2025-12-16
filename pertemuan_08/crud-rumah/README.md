# UTS - CRUD Data Rumah untuk Developer Perumahan

Aplikasi CRUD lengkap untuk mengelola data rumah dengan fitur upload foto, search, dan pagination menggunakan Flask dan MySQL.

## Deskripsi

Aplikasi web untuk developer perumahan dalam mengelola data rumah yang mencakup informasi lengkap seperti spesifikasi rumah, harga, lokasi, dan foto rumah.

## Fitur

- CRUD lengkap (Create, Read, Update, Delete) data rumah
- Upload foto rumah
- Pencarian berdasarkan nama rumah atau alamat
- Pagination untuk membagi data menjadi beberapa halaman
- Desain responsif dengan Bootstrap 5.3.0

## Setup Database

```sql
CREATE DATABASE uts_rumah_db;
USE uts_rumah_db;

CREATE TABLE rumah (
    kode_rumah VARCHAR(50) PRIMARY KEY,
    nama_rumah VARCHAR(100) NOT NULL,
    alamat TEXT NOT NULL,
    harga BIGINT NOT NULL,
    luas_tanah INT NOT NULL,
    luas_bangunan INT NOT NULL,
    kamar_tidur INT NOT NULL,
    kamar_mandi INT NOT NULL,
    developer VARCHAR(100) NOT NULL,
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
app.config['MYSQL_DB'] = 'uts_rumah_db'
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses di browser: http://127.0.0.1:5000

## Struktur Folder

```
UTS/
└── crud-rumah/
    ├── app.py
    ├── README.md
    ├── templates/
    │   ├── index.html
    │   ├── add.html
    │   └── edit.html
    └── uploads/
        └── (file gambar tersimpan di sini)
```

## Struktur Data

Tabel `rumah` memiliki field:
- `kode_rumah` - Kode unik rumah (Primary Key)
- `nama_rumah` - Nama/tipe rumah
- `alamat` - Alamat lengkap rumah
- `harga` - Harga rumah (dalam Rupiah)
- `luas_tanah` - Luas tanah dalam m²
- `luas_bangunan` - Luas bangunan dalam m²
- `kamar_tidur` - Jumlah kamar tidur
- `kamar_mandi` - Jumlah kamar mandi
- `developer` - Nama developer/perumahan
- `filename` - Nama file foto rumah

## Format File yang Diizinkan

- JPG/JPEG
- PNG
- GIF

## Teknologi yang Digunakan

- Flask - Web framework
- Flask-MySQLdb - MySQL connector
- Bootstrap 5.3.0 - CSS framework
- Jinja2 - Template engine
- Werkzeug - File upload handling

## Referensi

Aplikasi ini dibuat berdasarkan materi dari:
- Pertemuan 3 - API dan JSON
- Pertemuan 4 - Routing dan Authentication
- Pertemuan 5 - CRUD dengan Flask & MySQL
- Pertemuan 6 - CRUD dengan Upload File
- Pertemuan 7 - Search dan Pagination

