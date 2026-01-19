# Templates Folder

Folder ini berisi file template HTML untuk aplikasi CRUD Flask MySQL dengan fitur upload file.

## 📁 File Template

- **index.html** - Halaman utama untuk menampilkan daftar data stok dengan gambar
- **add.html** - Form untuk menambah data stok baru dengan upload gambar
- **edit.html** - Form untuk mengedit data stok dan update gambar

## 🎨 Template Engine

Template menggunakan **Jinja2** yang merupakan template engine default Flask.

## 📝 Fitur Template

- Bootstrap untuk styling
- Form handling dengan Flask (multipart/form-data untuk upload)
- Dynamic content rendering dengan gambar
- Image preview dan display
- Error message display

## 🔗 Cara Menggunakan

Template ini dirender oleh Flask menggunakan fungsi `render_template()`:

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', data=data)
```

## 📤 Upload File

Form upload menggunakan `enctype="multipart/form-data"`:

```html
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file" accept="image/*">
</form>
```

## 📚 Referensi

Lihat dokumentasi Flask tentang template: https://flask.palletsprojects.com/en/latest/templating/
