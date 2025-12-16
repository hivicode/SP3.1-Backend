# Pertemuan 9 - CRUD dengan MongoDB

Aplikasi CRUD sederhana menggunakan Flask dan MongoDB untuk mengelola data barang UMKM.

## Deskripsi

Aplikasi web untuk mengelola data barang UMKM dengan operasi CRUD lengkap menggunakan MongoDB sebagai database non-relasional.

## Fitur

- **CRUD Lengkap** (Create, Read, Update, Delete) data barang
- **MongoDB** sebagai database non-relasional
- **Flask-Bootstrap** untuk UI yang responsif
- Desain sederhana dan mudah digunakan

## Struktur Data

Collection `items` memiliki field:
- `kode` - Kode barang
- `nama` - Nama barang
- `harga` - Harga barang
- `jumlah` - Jumlah stok barang

## Setup Database

### 1. Install MongoDB

Pastikan MongoDB sudah terinstall dan berjalan di `localhost:27017`

### 2. Setup Database MongoDB

Database akan dibuat otomatis saat aplikasi pertama kali dijalankan:
- Database: `crud_database`
- Collection: `items`

Atau bisa dibuat manual dengan MongoDB Shell:
```javascript
use crud_database
db.items.insertOne({
    kode: "PRD001",
    nama: "Produk Sample",
    harga: 50000,
    jumlah: 10
})
```

## Instalasi

```bash
pip install flask flask-bootstrap pymongo
```

## Konfigurasi

Edit konfigurasi MongoDB di `app.py` jika perlu:

```python
client = MongoClient("mongodb://localhost:27017/")
db = client["crud_database"]
collection = db["items"]
```

## Menjalankan Aplikasi

```bash
python app.py
```

Akses di browser: http://127.0.0.1:5000

## Struktur Folder

```
pertemuan_9 (mongo)/
├── app.py
├── README.md
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── add.html
    └── edit.html
```

## Teknologi yang Digunakan

- **Flask** - Web framework
- **Flask-Bootstrap** - Bootstrap integration untuk Flask
- **PyMongo** - MongoDB driver untuk Python
- **MongoDB** - Database non-relasional
- **Jinja2** - Template engine

## Cara Menggunakan

1. Pastikan MongoDB service sudah berjalan
2. Jalankan aplikasi dengan `python app.py`
3. Buka browser dan akses http://127.0.0.1:5000
4. Gunakan menu untuk menambah, mengedit, atau menghapus data barang

## Catatan

- MongoDB harus berjalan di `localhost:27017` (default)
- Database dan collection akan dibuat otomatis saat pertama kali digunakan
- Data disimpan dalam format BSON di MongoDB

