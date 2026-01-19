# Pertemuan 8 - CRUD Data Rumah untuk Developer Perumahan

Aplikasi CRUD lengkap untuk mengelola data rumah dengan fitur upload foto, search, dan pagination menggunakan Flask dan MySQL.

## 📋 Deskripsi

Aplikasi web untuk developer perumahan dalam mengelola data rumah yang mencakup informasi lengkap seperti spesifikasi rumah, harga, lokasi, dan foto rumah. Aplikasi ini menggabungkan semua materi pembelajaran sebelumnya.

## 🚀 Fitur Utama

- **CRUD Lengkap**: Create, Read, Update, Delete data rumah
- **Upload Foto**: Upload dan kelola foto rumah
- **Pencarian**: Search berdasarkan nama rumah atau alamat
- **Pagination**: Membagi data menjadi beberapa halaman (5 item per halaman)
- **Responsive Design**: Desain responsif menggunakan Bootstrap 5.3.0
- **Form Validation**: Validasi input pada form

## 🗄️ Setup Database

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

## 📦 Install Dependencies

```bash
pip install flask flask-mysqldb werkzeug
```

## ⚙️ Konfigurasi

Edit file `app.py` sesuai dengan konfigurasi MySQL Anda:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'  # Ganti dengan password MySQL Anda
app.config['MYSQL_DB'] = 'uts_rumah_db'
```

## 🚀 Menjalankan Aplikasi

```bash
cd crud-rumah
python app.py
```

Akses aplikasi di browser: `http://127.0.0.1:5000`

## 📁 Struktur Folder

```
pertemuan_08/
├── README.md
└── crud-rumah/
    ├── app.py
    ├── insert_data.sql
    ├── README.md
    ├── templates/
    │   ├── index.html
    │   ├── add.html
    │   └── edit.html
    └── uploads/
        └── (file foto tersimpan di sini)
```

## 💡 Fitur yang Dipelajari

✅ CRUD lengkap dengan MySQL  
✅ Upload file gambar  
✅ Search dengan multiple fields  
✅ Pagination dengan navigasi  
✅ Form validation  
✅ File management (upload, delete)  
✅ Responsive design dengan Bootstrap  

## 🔍 Cara Menggunakan

### 1. Tambah Data Rumah
- Klik tombol "Tambah Data"
- Isi semua field form
- Upload foto rumah (opsional)
- Submit form

### 2. Cari Data
- Masukkan keyword di form search
- Klik "Cari" atau tekan Enter
- Hasil pencarian akan ditampilkan

### 3. Navigasi Halaman
- Gunakan tombol Previous/Next untuk berpindah halaman
- Data dibagi menjadi 5 item per halaman

### 4. Edit Data
- Klik tombol "Edit" pada data yang ingin diubah
- Update data dan/atau ganti foto
- Submit form

### 5. Hapus Data
- Klik tombol "Hapus" pada data yang ingin dihapus
- Data dan file foto akan dihapus

## 📤 Format File yang Diizinkan

- JPG/JPEG
- PNG
- GIF

## 🛠️ Teknologi

- **Flask** - Web framework
- **Flask-MySQLdb** - MySQL connector
- **Werkzeug** - File upload handling
- **Bootstrap 5.3.0** - CSS framework
- **Jinja2** - Template engine

## 📊 Struktur Data

Tabel `rumah` memiliki field:
- `kode_rumah` (VARCHAR, PRIMARY KEY) - Kode unik rumah
- `nama_rumah` (VARCHAR) - Nama/tipe rumah
- `alamat` (TEXT) - Alamat lengkap
- `harga` (BIGINT) - Harga rumah
- `luas_tanah` (INT) - Luas tanah dalam m²
- `luas_bangunan` (INT) - Luas bangunan dalam m²
- `kamar_tidur` (INT) - Jumlah kamar tidur
- `kamar_mandi` (INT) - Jumlah kamar mandi
- `developer` (VARCHAR) - Nama developer
- `filename` (VARCHAR) - Nama file foto

## 📝 Catatan Penting

- Folder `uploads/` akan dibuat otomatis jika belum ada
- File disimpan dengan nama yang aman menggunakan `secure_filename()`
- File lama akan dihapus saat data dihapus atau foto diganti
- Search mencari di field `nama_rumah` dan `alamat`
- Pagination menggunakan 5 item per halaman

## 🎯 Tujuan Pembelajaran

1. Menggabungkan semua materi pembelajaran sebelumnya
2. Membuat aplikasi CRUD lengkap dengan fitur lengkap
3. Implementasi search dan pagination pada data kompleks
4. File management yang baik
5. Form handling dengan multiple fields
6. Responsive design untuk aplikasi real-world

## 📚 Referensi Materi

Aplikasi ini dibuat berdasarkan referensi dari:
- **Pertemuan 3** - API dan JSON
- **Pertemuan 4** - Routing dan Authentication
- **Pertemuan 5** - CRUD dengan Flask & MySQL
- **Pertemuan 6** - CRUD dengan Upload File
- **Pertemuan 7** - Search dan Pagination

## 🔐 Keamanan

- ✅ Validasi ekstensi file
- ✅ Menggunakan `secure_filename()` untuk mencegah path traversal
- ✅ Form validation
- ⚠️ Untuk production, tambahkan validasi ukuran file
- ⚠️ Untuk production, tambahkan CSRF protection

