# Pertemuan 5 — CRUD Flask + MySQL

Aplikasi contoh CRUD menggunakan Flask dan MySQL, berada di folder `pertemuan_5/crud-flask-mysql/`.

## Requirements

- Python 3.8+
- MySQL Server (lokal atau remote)
- Paket Python: `flask`, `flask-mysqldb`

Install paket Python:

```bash
pip install flask flask-mysqldb
```

## Konfigurasi Database

1. Buat database dan tabel:

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

2. Sesuaikan kredensial MySQL di `pertemuan_5/crud-flask-mysql/app.py` jika perlu:
   - `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DB`

Default di kode:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crud_db'
```

## Menjalankan Aplikasi

Jalankan dari folder `pertemuan_5/crud-flask-mysql/`:

```bash
python app.py
```

Secara default berjalan di `http://127.0.0.1:5000`.

## Struktur Fitur

- `GET /` menampilkan daftar data `stok` (render `templates/index.html`).
- `GET /add` form tambah data (render `templates/add.html`).
- `POST /add` simpan data baru ke tabel `stok`.
- `GET /edit/<id>` form edit data berdasarkan `kode`.
- `POST /edit/<id>` simpan perubahan data.
- `GET /delete/<id>` hapus data berdasarkan `kode`.

## Template

File HTML berada di `pertemuan_5/crud-flask-mysql/templates/`:

- `index.html` — daftar data
- `add.html` — form tambah
- `edit.html` — form edit

Pastikan tabel `stok` sudah dibuat sebelum menjalankan aplikasi.




