# Pertemuan 7 - CRUD Flask dengan Search dan Pagination

Aplikasi CRUD dengan fitur pencarian dan pagination menggunakan Flask dan MySQL.

## 📋 Deskripsi

Pertemuan ini membahas implementasi fitur pencarian (search) dan pagination pada aplikasi CRUD Flask dengan MySQL. Aplikasi mengelola data stok dengan kemampuan untuk mencari data dan membagi hasil menjadi beberapa halaman.

## 🚀 Fitur Utama

- **CRUD Lengkap**: Create, Read, Update, Delete data stok
- **Pencarian**: Search produk berdasarkan nama barang
- **Pagination**: Membagi data menjadi beberapa halaman (5 item per halaman)
- **Navigasi Halaman**: Tombol Previous dan Next untuk navigasi
- **Search Persistence**: Query pencarian tetap aktif saat berpindah halaman
- **Responsive Design**: Desain responsif menggunakan Bootstrap 5.3.0

## 🗄️ Setup Database

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

## 📦 Install Dependencies

```bash
pip install flask flask-mysqldb
```

## ⚙️ Konfigurasi

Edit file `app.py` sesuai dengan konfigurasi MySQL Anda:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'  # Ganti dengan password MySQL Anda
app.config['MYSQL_DB'] = 'crud_upload_db'
```

## 🚀 Menjalankan Aplikasi

```bash
cd crud-flask-search-pagination
python app.py
```

Akses aplikasi di browser: `http://127.0.0.1:5000`

## 📁 Struktur Folder

```
pertemuan_07/
├── README.md
└── crud-flask-search-pagination/
    ├── app.py
    ├── README.md
    └── templates/
        └── index.html
```

## 💡 Fitur yang Dipelajari

✅ Implementasi search dengan SQL LIKE  
✅ Pagination dengan LIMIT dan OFFSET  
✅ Query parameter handling dengan Flask  
✅ Search query persistence  
✅ Navigasi halaman dengan Previous/Next  
✅ Menghitung total halaman  
✅ Menampilkan informasi halaman saat ini  

## 🔍 Cara Menggunakan Search

1. Masukkan keyword di form search
2. Klik tombol "Cari" atau tekan Enter
3. Hasil pencarian akan ditampilkan
4. Query search tetap aktif saat berpindah halaman

## 📄 Cara Menggunakan Pagination

1. Data otomatis dibagi menjadi beberapa halaman (5 item per halaman)
2. Gunakan tombol "Previous" untuk ke halaman sebelumnya
3. Gunakan tombol "Next" untuk ke halaman berikutnya
4. Tombol akan disabled jika sudah di halaman pertama/terakhir

## 🛠️ Teknologi

- **Flask** - Web framework
- **Flask-MySQLdb** - MySQL connector
- **Bootstrap 5.3.0** - CSS framework
- **Jinja2** - Template engine

## 📝 Catatan Penting

- Pagination menggunakan 5 item per halaman (bisa diubah di kode)
- Search menggunakan SQL LIKE dengan case-insensitive
- Query parameter `search` dan `page` digunakan untuk state management
- Pastikan database sudah berisi data untuk melihat pagination bekerja

## 🎯 Tujuan Pembelajaran

1. Memahami konsep pagination
2. Implementasi search dengan SQL
3. Query parameter handling
4. State management dengan URL parameters
5. Menghitung total halaman
6. Navigasi antar halaman

## 💻 Contoh Query SQL

### Search Query
```sql
SELECT * FROM stok 
WHERE nama LIKE '%keyword%' 
LIMIT 5 OFFSET 0
```

### Pagination Query
```sql
SELECT * FROM stok 
LIMIT 5 OFFSET 10  -- Halaman 3 (offset = (page-1) * per_page)
```

## 🔧 Customization

Untuk mengubah jumlah item per halaman, edit di `app.py`:

```python
PER_PAGE = 5  # Ubah angka ini
```

## 📊 Struktur Data

Tabel `stok` memiliki field:
- `kode` (VARCHAR, PRIMARY KEY)
- `nama` (VARCHAR)
- `harga` (INT)

