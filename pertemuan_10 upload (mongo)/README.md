# Pertemuan 10 - CRUD dengan MongoDB + Upload File

Aplikasi CRUD lengkap untuk mengelola data rumah dengan fitur upload foto menggunakan Flask dan MongoDB.

## Deskripsi

Aplikasi web untuk developer perumahan dalam mengelola data rumah yang mencakup informasi lengkap seperti spesifikasi rumah, harga, lokasi, dan foto rumah menggunakan MongoDB sebagai database.

## Fitur

- **CRUD Lengkap** (Create, Read, Update, Delete) data rumah
- **Upload Foto** rumah dengan validasi ekstensi file
- **MongoDB** sebagai database non-relasional
- **Unique Index** pada field `kode_rumah` (Primary Key)
- **Kode rumah tidak bisa diubah** setelah dibuat
- Desain responsif dengan Bootstrap 5.3.0

## Struktur Data

Collection `rumah` di database `perumahan` memiliki field:
- `kode_rumah` - Kode unik rumah (Primary Key, Unique Index)
- `nama_rumah` - Nama/tipe rumah
- `alamat` - Alamat lengkap rumah
- `harga` - Harga rumah (dalam Rupiah)
- `luas_tanah` - Luas tanah dalam m²
- `luas_bangunan` - Luas bangunan dalam m²
- `kamar_tidur` - Jumlah kamar tidur
- `kamar_mandi` - Jumlah kamar mandi
- `developer` - Nama developer/perumahan
- `filename` - Nama file foto rumah

## Setup Database

### 1. Install MongoDB

Pastikan MongoDB sudah terinstall dan berjalan di `localhost:27017`

### 2. Setup Database MongoDB

Database akan dibuat otomatis saat aplikasi pertama kali dijalankan:
- Database: `perumahan`
- Collection: `rumah`
- Unique Index: `kode_rumah`

Atau bisa setup manual dengan MongoDB Shell:
```javascript
use perumahan
db.rumah.createIndex("kode_rumah", { unique: true })
```

### 3. Insert Data Sample (Opsional)

Jalankan script untuk insert data sample:
```bash
python insert_data.py
```

Script akan membuat tabel dan insert 25 data rumah sample.

## Instalasi

```bash
pip install flask pymongo werkzeug
```

## Konfigurasi

Edit konfigurasi MongoDB di `app.py` jika perlu:

```python
client = MongoClient("mongodb://localhost:27017/")
db = client["perumahan"]
collection = db["rumah"]
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses di browser: http://127.0.0.1:5000

## Struktur Folder

```
pertemuan_10 upload (mongo)/
├── app.py
├── insert_data.py
├── README.md
├── static/
│   └── uploads/
│       └── (file gambar tersimpan di sini)
└── templates/
    ├── index.html
    ├── add.html
    └── edit.html
```

## Format File yang Diizinkan

- PNG
- JPG/JPEG
- GIF
- WEBP
- SVG

## Teknologi yang Digunakan

- **Flask** - Web framework
- **PyMongo** - MongoDB driver untuk Python
- **MongoDB** - Database non-relasional
- **Werkzeug** - File upload handling
- **Bootstrap 5.3.0** - CSS framework
- **Jinja2** - Template engine

## Fitur Khusus

### Unique Index pada Kode Rumah
- Field `kode_rumah` memiliki unique index untuk mencegah duplikasi
- Kode rumah tidak bisa diubah setelah dibuat (readonly di form edit)

### Upload File
- Validasi ekstensi file sebelum upload
- File disimpan di folder `static/uploads/`
- Folder uploads dibuat otomatis jika belum ada

## Cara Menggunakan

1. Pastikan MongoDB service sudah berjalan
2. Jalankan aplikasi dengan `python app.py`
3. Buka browser dan akses http://127.0.0.1:5000
4. Gunakan menu untuk menambah, mengedit, atau menghapus data rumah
5. Upload foto rumah saat menambah atau mengedit data

## Catatan

- MongoDB harus berjalan di `localhost:27017` (default)
- Database dan collection akan dibuat otomatis saat pertama kali digunakan
- Folder `static/uploads/` akan dibuat otomatis untuk menyimpan file gambar
- Kode rumah harus unik dan tidak bisa diubah setelah dibuat




