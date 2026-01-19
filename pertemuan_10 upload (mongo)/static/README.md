# Static Folder

Folder ini berisi file static (CSS, JavaScript, images) dan folder uploads untuk aplikasi CRUD dengan MongoDB.

## 📁 Struktur Folder

```
static/
├── uploads/          # Folder untuk menyimpan file foto rumah yang diupload
└── README.md
```

## 📤 Uploads Folder

Folder `static/uploads/` digunakan untuk menyimpan file foto rumah yang diupload melalui aplikasi.

### Format File yang Diizinkan
- PNG
- JPG/JPEG
- GIF
- WEBP
- SVG

### Keamanan
- File disimpan dengan nama yang aman menggunakan `secure_filename()` dari Werkzeug
- Validasi ekstensi file dilakukan sebelum upload
- Folder akan dibuat otomatis jika belum ada

## 🔗 Cara Menggunakan

File static diakses melalui URL path `/static/`:

```html
<img src="{{ url_for('static', filename='uploads/filename.jpg') }}">
```

Atau langsung:

```html
<img src="/static/uploads/filename.jpg">
```

## 📝 Catatan

- Folder `uploads/` akan dibuat otomatis saat aplikasi pertama kali dijalankan
- File lama akan dihapus saat data dihapus atau foto diganti
- Jangan hapus file secara manual kecuali yakin file tersebut tidak digunakan lagi

## 📚 Referensi

Lihat dokumentasi Flask tentang static files: https://flask.palletsprojects.com/en/latest/tutorial/static/
