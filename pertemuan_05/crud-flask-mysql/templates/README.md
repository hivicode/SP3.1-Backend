# Templates Folder

Folder ini berisi file template HTML untuk aplikasi CRUD Flask MySQL.

## ?? File Template

- **index.html** - Halaman utama untuk menampilkan daftar data stok
- **add.html** - Form untuk menambah data stok baru
- **edit.html** - Form untuk mengedit data stok yang sudah ada

## ?? Template Engine

Template menggunakan **Jinja2** yang merupakan template engine default Flask.

## ?? Fitur Template

- Bootstrap untuk styling
- Form handling dengan Flask
- Dynamic content rendering
- Error message display

## ?? Cara Menggunakan

Template ini dirender oleh Flask menggunakan fungsi `render_template()`:

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', data=data)
```

## ?? Referensi

Lihat dokumentasi Flask tentang template: https://flask.palletsprojects.com/en/latest/templating/
