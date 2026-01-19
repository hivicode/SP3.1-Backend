# Static Folder

Folder ini berisi file static (CSS, JavaScript, images) untuk aplikasi.

## 📁 Struktur Folder

```
static/
├── uploads/          # Folder untuk menyimpan file yang diupload
└── README.md
```

## 📤 Uploads Folder

Folder `static/uploads/` digunakan untuk menyimpan file yang diupload melalui aplikasi.

## 🔗 Cara Menggunakan

File static diakses melalui URL path `/static/`:

```html
<img src="{{ url_for('static', filename='uploads/filename.jpg') }}">
```

Atau langsung:

```html
<img src="/static/uploads/filename.jpg">
```

## 📚 Referensi

Lihat dokumentasi Flask tentang static files: https://flask.palletsprojects.com/en/latest/tutorial/static/
