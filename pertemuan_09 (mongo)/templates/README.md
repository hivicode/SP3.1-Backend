# Templates Folder

Folder ini berisi file template HTML untuk aplikasi CRUD dengan MongoDB.

## 📁 File Template

- **index.html** - Halaman utama untuk menampilkan daftar data barang UMKM
- **add.html** - Form untuk menambah data barang baru
- **edit.html** - Form untuk mengedit data barang yang sudah ada

## 🎨 Template Engine

Template menggunakan **Jinja2** yang merupakan template engine default Flask.

## 📝 Fitur Template

- Flask-Bootstrap untuk styling dan UI components
- Form handling dengan Flask
- Dynamic content rendering
- Bootstrap components (cards, buttons, forms)
- Error message display

## 🔗 Cara Menggunakan

Template ini dirender oleh Flask menggunakan fungsi `render_template()`:

```python
from flask import render_template

@app.route('/')
def index():
    items = collection.find()
    return render_template('index.html', items=items)
```

## 📚 Referensi

Lihat dokumentasi Flask tentang template: https://flask.palletsprojects.com/en/latest/templating/
