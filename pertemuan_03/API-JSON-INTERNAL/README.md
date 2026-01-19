# API JSON Internal

Aplikasi Flask yang menggunakan data JSON internal (in-memory) dengan operasi CRUD simulasi.

## 📋 Deskripsi

Aplikasi ini mendemonstrasikan cara menggunakan data JSON yang disimpan secara internal dalam aplikasi (in-memory). Data tidak disimpan di file eksternal, melainkan langsung di dalam kode Python sebagai dictionary/list.

## 🚀 Fitur

- **GET /** - Mendapatkan data karyawan
- **GET /karyawan** - Mendapatkan data karyawan
- **POST /karyawan** - Menambah data karyawan (simulasi)
- **PUT /karyawan** - Update data karyawan (simulasi)
- **DELETE /karyawan** - Hapus data karyawan (simulasi)

## 📁 File

- `app-json.py` - Aplikasi Flask utama dengan data internal

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

### GET / atau GET /karyawan
Mendapatkan semua data karyawan.

**Response:**
```json
[
  {
    "id": 1,
    "nama": "John Doe",
    "jabatan": "Developer",
    "gaji": 5000000
  },
  ...
]
```

### POST /karyawan
Menambah data karyawan baru (simulasi - data tidak benar-benar disimpan).

**Request:**
```bash
curl -X POST http://localhost:5000/karyawan
```

**Response:**
```json
{
  "message": "Data karyawan berhasil ditambahkan"
}
```

### PUT /karyawan
Update data karyawan (simulasi).

**Request:**
```bash
curl -X PUT http://localhost:5000/karyawan
```

**Response:**
```json
{
  "message": "Data karyawan berhasil diupdate"
}
```

### DELETE /karyawan
Hapus data karyawan (simulasi).

**Request:**
```bash
curl -X DELETE http://localhost:5000/karyawan
```

**Response:**
```json
{
  "message": "Data karyawan berhasil dihapus"
}
```

## 💡 Konsep yang Dipelajari

✅ Data JSON internal (in-memory)  
✅ RESTful API dengan berbagai HTTP methods  
✅ Simulasi operasi CRUD  
✅ JSON response dengan `jsonify()`  
✅ HTTP methods: GET, POST, PUT, DELETE  

## 📝 Contoh Request

### Menggunakan curl

```bash
# Get all employees
curl http://localhost:5000/
curl http://localhost:5000/karyawan

# Create employee (simulation)
curl -X POST http://localhost:5000/karyawan

# Update employee (simulation)
curl -X PUT http://localhost:5000/karyawan

# Delete employee (simulation)
curl -X DELETE http://localhost:5000/karyawan
```

### Menggunakan Browser

Buka langsung di browser:
- `http://localhost:5000/` - Semua data
- `http://localhost:5000/karyawan` - Semua data (alternatif)

**Catatan:** Browser hanya bisa melakukan GET request. Untuk POST, PUT, DELETE gunakan tools seperti Postman atau curl.

## 🎯 Tujuan Pembelajaran

1. Memahami perbedaan data internal vs eksternal
2. Membuat RESTful API dengan berbagai HTTP methods
3. Simulasi operasi CRUD
4. Response format JSON untuk berbagai operasi
5. HTTP methods yang berbeda

## 📚 Struktur Data Internal

Data disimpan sebagai list of dictionaries dalam Python:

```python
karyawan = [
    {
        "id": 1,
        "nama": "John Doe",
        "jabatan": "Developer",
        "gaji": 5000000
    },
    ...
]
```

## ⚠️ Catatan Penting

- Data adalah simulasi, tidak benar-benar melakukan CRUD
- Data akan hilang saat aplikasi di-restart (karena in-memory)
- Untuk aplikasi real, gunakan database untuk persistensi data
- POST, PUT, DELETE hanya simulasi untuk demonstrasi HTTP methods

## 🔧 Tips

- Gunakan Postman atau Insomnia untuk test semua HTTP methods
- Perhatikan perbedaan response untuk setiap HTTP method
- Untuk implementasi real CRUD, perlu koneksi ke database

## 🔄 Perbandingan dengan API-JSON-EXTERNAL

| Aspek | JSON External | JSON Internal |
|-------|---------------|---------------|
| Sumber Data | File eksternal (`data.json`) | Data dalam kode Python |
| Persistensi | Data tersimpan di file | Data hilang saat restart |
| Operasi | Hanya READ | Simulasi CRUD lengkap |
| Use Case | Data statis | Demonstrasi HTTP methods |