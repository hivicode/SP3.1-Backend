# Tugas 1 - API Produk UMKM

Aplikasi Flask API untuk mengelola produk UMKM dengan kategori Snacks dan Drinks.

## 📋 Deskripsi

Aplikasi RESTful API untuk produk UMKM yang terbagi menjadi dua kategori: Snacks dan Drinks. Data produk disimpan dalam file JSON terpisah untuk setiap kategori.

## 🚀 Fitur

- **GET /** - Halaman welcome/homepage
- **GET /produk/snack** - Semua produk snack
- **GET /produk/drink** - Semua produk drink
- **GET /produk/snack/<id>** - Detail snack berdasarkan ID
- **GET /produk/drink/<id>** - Detail drink berdasarkan ID
- **Error Handling** - Error 404 jika produk tidak ditemukan

## 📁 File

- `api-produk.py` - Aplikasi Flask utama
- `snacks.json` - Data produk snack
- `drinks.json` - Data produk drink

## 📦 Instalasi

```bash
pip install flask
```

## 🚀 Menjalankan Aplikasi

```bash
python api-produk.py
```

Akses di browser: `http://127.0.0.1:5000`

## 🔌 API Endpoints

### GET /
Halaman welcome/homepage.

**Response:**
```json
{
  "message": "Welcome to UMKM Product API",
  "endpoints": {
    "snacks": "/produk/snack",
    "drinks": "/produk/drink"
  }
}
```

### GET /produk/snack
Mengambil semua produk snack.

**Response:**
```json
[
  {
    "id": 1,
    "nama": "Keripik Singkong",
    "harga": 15000,
    "stok": 50
  },
  ...
]
```

### GET /produk/drink
Mengambil semua produk drink.

**Response:**
```json
[
  {
    "id": 1,
    "nama": "Es Teh Manis",
    "harga": 5000,
    "stok": 100
  },
  ...
]
```

### GET /produk/snack/<id>
Mengambil detail snack berdasarkan ID.

**Response (Success):**
```json
{
  "id": 1,
  "nama": "Keripik Singkong",
  "harga": 15000,
  "stok": 50
}
```

**Response (Error 404):**
```json
{
  "error": "Produk snack tidak ditemukan"
}
```

### GET /produk/drink/<id>
Mengambil detail drink berdasarkan ID.

**Response:** Similar dengan snack endpoint

## 💡 Konsep yang Dipelajari

✅ Routing dengan multiple paths  
✅ Dynamic routing dengan parameter  
✅ Kategori produk (snack/drink)  
✅ Multiple JSON files  
✅ Error handling  
✅ JSON response dengan `jsonify()`  
✅ Organisasi data berdasarkan kategori  

## 📝 Contoh Request

### Menggunakan curl

```bash
# Welcome page
curl http://localhost:5000/

# Get all snacks
curl http://localhost:5000/produk/snack

# Get all drinks
curl http://localhost:5000/produk/drink

# Get snack by ID
curl http://localhost:5000/produk/snack/1

# Get drink by ID
curl http://localhost:5000/produk/drink/1
```

### Menggunakan Browser

Buka langsung di browser:
- `http://localhost:5000/` - Welcome page
- `http://localhost:5000/produk/snack` - Semua snack
- `http://localhost:5000/produk/drink` - Semua drink
- `http://localhost:5000/produk/snack/1` - Detail snack ID 1
- `http://localhost:5000/produk/drink/1` - Detail drink ID 1

## 🎯 Tujuan Pembelajaran

1. Membuat API dengan multiple endpoints
2. Routing dengan kategori
3. Dynamic routing dengan parameter
4. Mengelola multiple JSON files
5. Error handling untuk produk tidak ditemukan
6. Organisasi data berdasarkan kategori

## 📚 Struktur Data JSON

### snacks.json
```json
[
  {
    "id": 1,
    "nama": "Keripik Singkong",
    "harga": 15000,
    "stok": 50
  },
  ...
]
```

### drinks.json
```json
[
  {
    "id": 1,
    "nama": "Es Teh Manis",
    "harga": 5000,
    "stok": 100
  },
  ...
]
```

## ⚠️ Catatan Penting

- File `snacks.json` dan `drinks.json` harus berada di folder yang sama dengan `api-produk.py`
- ID harus unik dalam setiap kategori
- Data dibaca setiap kali ada request (tidak di-cache)
- File JSON harus valid, jika tidak aplikasi akan error

## 🔧 Tips

- Gunakan extension JSON Viewer di browser untuk melihat response yang rapi
- Test API menggunakan Postman atau Insomnia
- Pastikan file JSON memiliki format yang valid
- ID produk harus berupa angka

## 📊 Struktur Endpoint

```
/                           → Welcome page
/produk/snack               → Semua snack
/produk/snack/<id>         → Detail snack
/produk/drink              → Semua drink
/produk/drink/<id>         → Detail drink
```
