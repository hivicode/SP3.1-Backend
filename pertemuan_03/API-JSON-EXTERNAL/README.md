# API JSON External

Aplikasi Flask yang membaca dan menyajikan data dari file JSON eksternal melalui RESTful API.

## 📋 Deskripsi

Aplikasi ini mendemonstrasikan cara membaca data dari file JSON eksternal dan menyajikannya melalui API endpoints. Data disimpan dalam file `data.json` dan dibaca setiap kali ada request.

## 🚀 Fitur

- **GET /** - Mengambil semua data user
- **GET /<id>** - Mengambil data user berdasarkan ID
- **Error Handling** - Menampilkan error 404 jika ID tidak ditemukan
- **JSON Response** - Semua response dalam format JSON

## 📁 File

- `app-json.py` - Aplikasi Flask utama
- `data.json` - File JSON sebagai sumber data eksternal

## 📦 Instalasi

```bash
pip install flask
```

## 🚀 Menjalankan Aplikasi

```bash
python app-json.py
```

Akses di browser: `http://127.0.0.1:5000`

## 🔌 API Endpoints

### GET /
Mengambil semua data user dari file JSON.

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  ...
]
```

### GET /<id>
Mengambil data user berdasarkan ID.

**Response (Success):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

**Response (Error 404):**
```json
{
  "error": "User not found"
}
```

## 💡 Konsep yang Dipelajari

✅ Membaca file JSON eksternal  
✅ RESTful API dengan Flask  
✅ Dynamic routing dengan parameter  
✅ Error handling dengan HTTP status code  
✅ JSON response dengan `jsonify()`  
✅ File I/O dengan Python  

## 📝 Contoh Request

### Menggunakan curl

```bash
# Get all users
curl http://localhost:5000/

# Get user by ID
curl http://localhost:5000/1
```

### Menggunakan Browser

Buka langsung di browser:
- `http://localhost:5000/` - Semua data
- `http://localhost:5000/1` - Data dengan ID 1

## 🎯 Tujuan Pembelajaran

1. Memahami cara membaca file JSON dengan Python
2. Membuat RESTful API sederhana
3. Dynamic routing dengan parameter
4. Error handling pada API
5. Response format JSON

## 📚 Struktur Data JSON

File `data.json` harus memiliki format array of objects:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com"
  }
]
```

## ⚠️ Catatan Penting

- File `data.json` harus berada di folder yang sama dengan `app-json.py`
- Data dibaca setiap kali ada request (tidak di-cache)
- Untuk production, pertimbangkan untuk menggunakan database
- File JSON harus valid, jika tidak aplikasi akan error

## 🔧 Tips

- Gunakan extension JSON Viewer di browser untuk melihat response yang rapi
- Test API menggunakan Postman atau Insomnia untuk pengalaman yang lebih baik
- Pastikan file JSON memiliki format yang valid sebelum menjalankan aplikasi