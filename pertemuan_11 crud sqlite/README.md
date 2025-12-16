# Pertemuan 11 - CRUD dengan SQLite + Upload File

Aplikasi CRUD lengkap untuk mengelola data rumah dengan fitur upload foto, search, dan pagination menggunakan Flask dan SQLite.

## Deskripsi

Aplikasi web untuk developer perumahan dalam mengelola data rumah yang mencakup informasi lengkap seperti spesifikasi rumah, harga, lokasi, dan foto rumah menggunakan SQLite sebagai database file-based.

## Fitur

- **CRUD Lengkap** (Create, Read, Update, Delete) data rumah
- **Upload Foto** rumah dengan validasi ekstensi file
- **Pencarian** berdasarkan nama rumah atau alamat
- **Pagination** untuk membagi data menjadi beberapa halaman
- **SQLite** sebagai database file-based (tidak perlu server terpisah)
- **Kode rumah sebagai Primary Key** (tidak bisa diubah setelah dibuat)
- Desain responsif dengan Bootstrap 5.3.0

## Struktur Database

Tabel `rumah` di database `perumahan.db` memiliki field:
- `kode_rumah` - Kode unik rumah (Primary Key, TEXT)
- `nama_rumah` - Nama/tipe rumah (TEXT NOT NULL)
- `alamat` - Alamat lengkap rumah (TEXT NOT NULL)
- `harga` - Harga rumah dalam Rupiah (INTEGER NOT NULL)
- `luas_tanah` - Luas tanah dalam m² (INTEGER NOT NULL)
- `luas_bangunan` - Luas bangunan dalam m² (INTEGER NOT NULL)
- `kamar_tidur` - Jumlah kamar tidur (INTEGER NOT NULL)
- `kamar_mandi` - Jumlah kamar mandi (INTEGER NOT NULL)
- `developer` - Nama developer/perumahan (TEXT NOT NULL)
- `filename` - Nama file foto rumah (TEXT)

## Setup Database

### 1. Database SQLite

Database SQLite akan dibuat otomatis saat aplikasi pertama kali dijalankan:
- File database: `perumahan.db` (di folder aplikasi)
- Tabel `rumah` akan dibuat otomatis dengan struktur di atas

### 2. Insert Data Sample (Opsional)

Untuk insert data sample, buat script Python sederhana:

```python
import sqlite3

conn = sqlite3.connect('perumahan.db')
cursor = conn.cursor()

cursor.execute("""
    INSERT INTO rumah (kode_rumah, nama_rumah, alamat, harga, luas_tanah, luas_bangunan, kamar_tidur, kamar_mandi, developer, filename)
    VALUES ('R001', 'Griya Sejahtera A1', 'Jl. Melati No. 12, Bandung', 850000000, 120, 90, 3, 2, 'PT Maju Jaya', 'rumah_a1.jpg')
""")
conn.commit()
conn.close()
```

## Instalasi

```bash
pip install flask werkzeug
```

**Catatan:** SQLite sudah built-in di Python, tidak perlu install library tambahan.

## Konfigurasi

Database SQLite menggunakan file lokal `perumahan.db` di folder aplikasi. Path database sudah dikonfigurasi otomatis di `app.py`:

```python
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "perumahan.db")
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses di browser: http://127.0.0.1:5000

## Struktur Folder

```
pertemuan_11 crud sqlite/
├── app.py
├── perumahan.db
├── README.md
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
└── uploads/
    └── (file gambar tersimpan di sini)
```

## Format File yang Diizinkan

- JPG/JPEG
- PNG
- GIF

## Teknologi yang Digunakan

- **Flask** - Web framework
- **SQLite3** - Database file-based (built-in Python)
- **Werkzeug** - File upload handling
- **Bootstrap 5.3.0** - CSS framework
- **Jinja2** - Template engine

## Fitur Khusus

### SQLite Database
- Database disimpan sebagai file `perumahan.db` di folder aplikasi
- Tidak perlu install server database terpisah
- Database dan tabel dibuat otomatis saat pertama kali dijalankan

### Search dan Pagination
- Pencarian berdasarkan nama rumah atau alamat
- Pagination dengan 5 data per halaman
- Navigasi Previous/Next dan nomor halaman

### Upload File
- Validasi ekstensi file sebelum upload
- File disimpan di folder `uploads/`
- Folder uploads dibuat otomatis jika belum ada

## Cara Menggunakan

1. Jalankan aplikasi dengan `python app.py`
2. Buka browser dan akses http://127.0.0.1:5000
3. Gunakan form search untuk mencari data rumah
4. Gunakan pagination untuk navigasi antar halaman
5. Gunakan menu untuk menambah, mengedit, atau menghapus data rumah
6. Upload foto rumah saat menambah atau mengedit data

## Keuntungan SQLite

- **Tidak perlu server** - Database adalah file lokal
- **Mudah digunakan** - Tidak perlu konfigurasi kompleks
- **Portable** - File database bisa dipindah dengan mudah
- **Cocok untuk development** - Ideal untuk aplikasi kecil hingga menengah

## Catatan

- File database `perumahan.db` akan dibuat otomatis di folder aplikasi
- Folder `uploads/` akan dibuat otomatis untuk menyimpan file gambar
- Kode rumah adalah Primary Key dan tidak bisa diubah setelah dibuat
- SQLite cocok untuk aplikasi single-user atau development, untuk production dengan banyak user concurrent disarankan menggunakan PostgreSQL atau MySQL

