# UTS - CRUD Data Rumah untuk Developer Perumahan

## Deskripsi

Aplikasi UTS untuk mengelola data rumah bagi developer perumahan dengan fitur CRUD lengkap, upload foto, search, dan pagination.

## Fitur Utama

- **CRUD Lengkap**: Create, Read, Update, Delete data rumah
- **Upload Foto**: Upload dan kelola foto rumah
- **Pencarian**: Search berdasarkan nama rumah atau alamat
- **Pagination**: Membagi data menjadi beberapa halaman (5 item per halaman)
- **Responsive Design**: Desain responsif menggunakan Bootstrap 5.3.0

## Setup Database

Buat database dan tabel dengan menjalankan SQL berikut:

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
app.config['MYSQL_DB'] = 'uts_rumah_db'
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses aplikasi di browser: `http://127.0.0.1:5000`

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
```

## Teknologi

- Flask
- Flask-MySQLdb
- Bootstrap 5.3.0
- Jinja2
- Werkzeug

## Referensi Materi

Aplikasi ini dibuat berdasarkan referensi dari:
- Pertemuan 3 - API dan JSON
- Pertemuan 4 - Routing dan Authentication
- Pertemuan 5 - CRUD dengan Flask & MySQL
- Pertemuan 6 - CRUD dengan Upload File
- Pertemuan 7 - Search dan Pagination

