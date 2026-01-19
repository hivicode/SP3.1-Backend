# SP3.1 Backend

Repository ini berisi materi pembelajaran Backend Development dengan Flask dan Python.

## Struktur Materi

### Pertemuan 3 - API dan JSON
Mempelajari pembuatan RESTful API dengan Flask dan pengelolaan data JSON.

- API JSON External
- API JSON Internal
- Tugas 1: API Produk

[Lihat README lengkap](pertemuan_03/README.md)

### Pertemuan 4 - Routing dan Authentication
Mempelajari sistem routing dan autentikasi dalam Flask.

- Routing App
- Decorator App
- Test: Routing + Login

[Lihat README lengkap](pertemuan_04/README.md)

### Pertemuan 5 - CRUD dengan Flask & MySQL
Mempelajari operasi CRUD terhubung ke database MySQL menggunakan flask-mysqldb.

- CRUD Flask MySQL

[Lihat README lengkap](pertemuan_05/README.md)

### Pertemuan 6 - CRUD dengan Upload File
Mempelajari operasi CRUD dengan fitur upload file gambar.

- CRUD Flask MySQL dengan Upload File

[Lihat README lengkap](pertemuan_06/README.md)

### Pertemuan 7 - Search dan Pagination
Mempelajari implementasi fitur pencarian dan pagination pada aplikasi CRUD.

- CRUD Flask dengan Search dan Pagination

[Lihat README lengkap](pertemuan_07/README.md)

### Pertemuan 8 - CRUD Data Rumah dengan MySQL
Aplikasi CRUD lengkap untuk mengelola data rumah dengan MySQL.

- CRUD Data Rumah dengan Upload Foto

[Lihat README lengkap](pertemuan_08/README.md)

### Pertemuan 9 - CRUD dengan MongoDB
Mempelajari operasi CRUD menggunakan MongoDB sebagai database non-relasional.

- CRUD Flask dengan MongoDB (tanpa upload)

[Lihat README lengkap](pertemuan_9%20(mongo)/README.md)

### Pertemuan 10 - CRUD dengan MongoDB + Upload File
Mempelajari operasi CRUD dengan MongoDB dan fitur upload file.

- CRUD Flask dengan MongoDB + Upload File

[Lihat README lengkap](pertemuan_10%20upload%20(mongo)/README.md)

### Pertemuan 11 - CRUD dengan SQLite + Upload File
Mempelajari operasi CRUD menggunakan SQLite sebagai database file-based.

- CRUD Flask dengan SQLite + Upload File + Search + Pagination

[Lihat README lengkap](pertemuan_11%20crud%20sqlite/README.md)

### Pertemuan 8 UTS - CRUD Data Rumah untuk Developer Perumahan
Aplikasi UTS yang menggabungkan semua materi pembelajaran dengan fitur CRUD lengkap, upload foto, search, dan pagination menggunakan MySQL.

- CRUD Data Rumah dengan Upload Foto, Search, dan Pagination

[Lihat README lengkap](pertemuan_08%20UTS/README.md)

### UAS Project Perumahan
Aplikasi final project untuk sistem manajemen perumahan dengan backend API dan frontend terpisah.

- Backend API dengan SQLite
- Frontend dengan HTML, CSS, dan JavaScript

[Lihat README lengkap](UAS%20Project%20Perumahan/README.md)

## Quick Start

1. Clone repository ini
2. Install dependencies:
```bash
pip install flask
```
3. Masuk ke folder pertemuan yang diinginkan
4. Baca README.md di setiap folder untuk penjelasan detail
5. Jalankan file Python yang ada

## Struktur Folder

```
SP3.1-Backend/
├── README.md
├── pertemuan_3/
│   ├── README.md
│   ├── API-JSON-EXTERNAL/
│   ├── API-JSON-INTERNAL/
│   └── Tugas 1/
├── pertemuan_4/
│   ├── README.md
│   ├── ROUTING-APP/
│   ├── DECORATOR-APP/
│   └── TEST/
├── pertemuan_5/
│   ├── README.md
│   └── crud-flask-mysql/
├── pertemuan_6/
│   ├── README.md
│   └── crud-flask-mysql-upload/
├── pertemuan_7/
│   ├── README.md
│   └── crud-flask-search-pagination/
├── pertemuan_8/
│   ├── README.md
│   └── crud-rumah/
├── pertemuan_9 (mongo)/
│   ├── README.md
│   ├── app.py
│   ├── templates/
│   └── static/
├── pertemuan_10 upload (mongo)/
│   ├── README.md
│   ├── app.py
│   ├── insert_data.py
│   ├── templates/
│   └── static/
├── pertemuan_11 crud sqlite/
│   ├── README.md
│   ├── app.py
│   ├── perumahan.db
│   ├── templates/
│   └── uploads/
├── pertemuan_08 UTS/
│   ├── README.md
│   └── crud-rumah/
└── UAS Project Perumahan/
    ├── README.md
    ├── Backend/
    │   └── README.md
    └── Frontend/
        └── README.md
```

## Requirements

- Python 3.6+
- Flask
- Flask-MySQLdb (untuk Pertemuan 5, 6, 7, 8, dan UTS)
- MySQL Server (untuk Pertemuan 5, 6, 7, 8, dan UTS)
- MongoDB (untuk Pertemuan 9 dan 10)
- SQLite3 (built-in Python, untuk Pertemuan 11)

## Instalasi Dependencies

### Dependencies Umum
```bash
pip install flask
```

### Untuk MySQL (Pertemuan 5, 6, 7, 8, UTS)
```bash
pip install flask-mysqldb
# atau alternatif:
pip install mysql-connector-python
```

### Untuk MongoDB (Pertemuan 9, 10)
```bash
pip install pymongo flask-bootstrap
```

### Untuk SQLite (Pertemuan 11)
SQLite sudah built-in di Python, tidak perlu install tambahan.

### Install Semua Dependencies
```bash
pip install flask flask-mysqldb pymongo flask-bootstrap werkzeug
```

## Cara Menggunakan

Setiap folder pertemuan memiliki:
- README.md dengan penjelasan detail
- Contoh kode aplikasi Flask
- File HTML template
- File JSON data (untuk Pertemuan 3)

Baca README.md di setiap folder untuk penjelasan lengkap dan cara menjalankan aplikasi.

## About

Repository pembelajaran Backend Development menggunakan Flask Framework.


