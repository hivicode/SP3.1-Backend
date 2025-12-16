# Pertemuan 3 - API dan JSON

Materi pembelajaran pembuatan RESTful API dengan Flask dan pengelolaan data JSON.

## 📚 Daftar Materi

### 1. API-JSON-EXTERNAL
Membaca data dari file JSON eksternal dan menyajikannya melalui API.

### 2. API-JSON-INTERNAL
Mengelola data JSON secara internal (in-memory) dengan operasi CRUD.

### 3. Tugas 1 - API Produk UMKM
Implementasi API untuk produk UMKM dengan kategori Snacks dan Drinks.

## 🚀 Cara Menjalankan

### API-JSON-EXTERNAL

```bash
cd API-JSON-EXTERNAL
python app-json.py
```

**Endpoints:**
- `GET /` - Mengambil semua data user
- `GET /<id>` - Mengambil data user berdasarkan ID

**Contoh Request:**
```bash
curl http://localhost:5000/
curl http://localhost:5000/1
```

**File yang digunakan:**
- `app-json.py` - Aplikasi Flask
- `data.json` - Data user dalam format JSON

---

### API-JSON-INTERNAL

```bash
cd API-JSON-INTERNAL
python app-json.py
```

**Endpoints:**
- `GET /` - Mendapatkan data karyawan
- `GET /karyawan` - Mendapatkan data karyawan
- `POST /karyawan` - Menambah data karyawan (simulasi)
- `PUT /karyawan` - Update data karyawan (simulasi)
- `DELETE /karyawan` - Hapus data karyawan (simulasi)

**Contoh Request:**
```bash
curl http://localhost:5000/
curl -X GET http://localhost:5000/karyawan
curl -X POST http://localhost:5000/karyawan
curl -X PUT http://localhost:5000/karyawan
curl -X DELETE http://localhost:5000/karyawan
```

---

### Tugas 1 - API Produk UMKM

```bash
cd "Tugas 1"
python api-produk.py
```

**Endpoints:**
- `GET /` - Halaman utama/welcome
- `GET /produk/snack` - Semua produk snack
- `GET /produk/drink` - Semua produk drink
- `GET /produk/snack/<id>` - Detail snack berdasarkan ID
- `GET /produk/drink/<id>` - Detail drink berdasarkan ID

**Contoh Request:**
```bash
curl http://localhost:5000/
curl http://localhost:5000/produk/snack
curl http://localhost:5000/produk/drink
curl http://localhost:5000/produk/snack/1
curl http://localhost:5000/produk/drink/1
```

**File yang digunakan:**
- `api-produk.py` - Aplikasi Flask
- `snacks.json` - Data produk snack
- `drinks.json` - Data produk drink

## 💡 Fitur yang Dipelajari

✅ Membuat RESTful API dengan Flask  
✅ Operasi CRUD (Create, Read, Update, Delete)  
✅ Membaca data dari file JSON eksternal  
✅ Mengelola data JSON internal  
✅ Error handling dengan HTTP status code  
✅ Routing dengan parameter dinamis  
✅ Response JSON dengan `jsonify()`  

## 📝 Catatan Penting

- Semua aplikasi berjalan di port `5000` secara default
- Gunakan tools seperti Postman, Insomnia, atau curl untuk testing API
- Untuk melihat response yang rapi di browser, gunakan extension JSON Viewer
- File JSON harus berada di path yang sesuai dengan kode
- Error 404 akan muncul jika ID tidak ditemukan

## 🎯 Tujuan Pembelajaran

1. Memahami konsep RESTful API
2. Membuat endpoint dengan berbagai HTTP methods
3. Mengelola data dalam format JSON
4. Implementasi error handling
5. Routing dengan parameter dinamis
6. Membedakan data eksternal dan internal

## 🔧 Tips

- Pastikan Flask sudah terinstall: `pip install flask`
- Gunakan `debug=True` untuk development
- Periksa format JSON sebelum menjalankan aplikasi
- Gunakan Postman untuk testing API yang lebih mudah

