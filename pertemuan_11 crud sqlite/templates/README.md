# Templates Folder

Folder ini berisi file template HTML untuk aplikasi CRUD dengan SQLite, upload file, search, dan pagination.

## 📁 File Template

- **index.html** - Halaman utama dengan daftar data rumah, search form, dan pagination
- **add.html** - Form untuk menambah data rumah baru dengan upload foto
- **edit.html** - Form untuk mengedit data rumah dan update foto

## 🎨 Template Engine

Template menggunakan **Jinja2** yang merupakan template engine default Flask.

## 📝 Fitur Template

- Bootstrap 5.3.0 untuk styling
- Form handling dengan Flask (multipart/form-data untuk upload)
- Dynamic content rendering dengan gambar rumah
- Search functionality berdasarkan nama rumah atau alamat
- Pagination controls dengan 5 item per halaman
- Image preview dan display
- Responsive design

## 🔍 Fitur Search & Pagination

Template mendukung:
- Pencarian berdasarkan nama rumah atau alamat
- Pagination dengan 5 item per halaman
- Navigasi Previous/Next dan nomor halaman
- Search query persistence saat navigasi halaman

## 📤 Upload Foto

Form upload menggunakan `enctype="multipart/form-data"`:

```html
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file" accept="image/*">
</form>
```

## 🔗 Cara Menggunakan

Template ini dirender oleh Flask menggunakan fungsi `render_template()`:

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', rumah=rumah, search=search, page=page, total_pages=total_pages)
```

## 📚 Referensi

Lihat dokumentasi Flask tentang template: https://flask.palletsprojects.com/en/latest/templating/
