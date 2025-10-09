## API Produk UMKM — Tugas 1

Aplikasi Flask sederhana untuk menyajikan data produk UMKM dari berkas JSON (`snacks.json` dan `drinks.json`). Mendukung endpoint untuk melihat semua produk per kategori dan detail produk berdasarkan `id`.

### Struktur Berkas

- `api-produk.py`: Aplikasi Flask
- `snacks.json`: Data produk kategori snack
- `drinks.json`: Data produk kategori drink

### Prasyarat

- Python 3.8+
- Pip

Instal dependensi:

```bash
pip install Flask
```

### Cara Menjalankan

Karena kode membaca berkas JSON menggunakan path relatif `Tugas 1/...`, Anda harus menjalankan aplikasi dari direktori `Pertemuan_3` (BUKAN dari dalam folder `Tugas 1`).

1) Pindah ke direktori proyek pertemuan 3:

```bash
cd /home/bi/Documents/SP3.1-Backend/Pertemuan_3
```

2) Jalankan aplikasi:

```bash
python3 "Tugas 1/api-produk.py"
```

Server akan berjalan di `http://127.0.0.1:5000` (mode debug aktif).

### Endpoint

- GET `/` — Cek status API
- GET `/produk/snack` — Daftar semua snack
- GET `/produk/drink` — Daftar semua drink
- GET `/produk/snack/<id>` — Detail snack berdasarkan `id`
- GET `/produk/drink/<id>` — Detail drink berdasarkan `id`

### Contoh Penggunaan (cURL)

- Cek API:

```bash
curl http://127.0.0.1:5000/
```

Contoh respons:

```json
{"pesan":"Selamat Datang Di Produk UMKM"}
```

- Semua snack:

```bash
curl http://127.0.0.1:5000/produk/snack
```

Ringkasan respons:

```json
{
  "pesan": "Halaman Produk Semua Snack..",
  "data": [
    {"id":1, "nama":"Keripik Kentang", "harga":15000, ...},
    {"id":2, "nama":"Coklat", "harga":12000, ...}
  ]
}
```

- Detail snack id 1:

```bash
curl http://127.0.0.1:5000/produk/snack/1
```

Contoh respons:

```json
{
  "pesan": "Halaman Produk Snack dengan id = 1",
  "data": {
    "id": 1,
    "nama": "Keripik Kentang",
    "harga": 15000,
    "deskripsi": "Keripik kentang renyah dengan rasa asin",
    "kategori": "snack"
  }
}
```

- Semua drink:

```bash
curl http://127.0.0.1:5000/produk/drink
```

- Detail drink id 2:

```bash
curl http://127.0.0.1:5000/produk/drink/2
```

Jika `id` tidak ditemukan, server akan mengembalikan status `404` dengan pesan yang sesuai.

### Catatan

- Jalankan dari direktori `Pertemuan_3` agar path relatif `Tugas 1/snacks.json` dan `Tugas 1/drinks.json` terbaca dengan benar.
- Untuk perubahan data, sunting berkas JSON terkait dan restart server.


