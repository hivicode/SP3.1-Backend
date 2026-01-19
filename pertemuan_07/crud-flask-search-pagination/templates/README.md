# Templates Folder

Folder ini berisi file template HTML untuk aplikasi CRUD Flask dengan fitur search dan pagination.

## 📁 File Template

- **index.html** - Halaman utama dengan daftar data, search form, dan pagination

## 🎨 Template Engine

Template menggunakan **Jinja2** yang merupakan template engine default Flask.

## 📝 Fitur Template

- Bootstrap untuk styling
- Search form untuk pencarian data
- Pagination controls (Previous/Next buttons)
- Table display dengan data
- Dynamic content rendering
- Search query persistence saat navigasi halaman

## 🔍 Fitur Search

Template mendukung pencarian berdasarkan nama barang dengan form:

```html
<form method="GET" action="/">
    <input type="text" name="search" placeholder="Cari barang...">
    <button type="submit">Cari</button>
</form>
```

## 📄 Fitur Pagination

Pagination ditampilkan dengan:
- Tombol Previous (disabled jika di halaman pertama)
- Tombol Next (disabled jika di halaman terakhir)
- Informasi halaman saat ini

## 🔗 Cara Menggunakan

Template ini dirender oleh Flask menggunakan fungsi `render_template()`:

```python
from flask import render_template, request

@app.route('/')
def index():
    search = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    return render_template('index.html', data=data, search=search, page=page)
```

## 📚 Referensi

Lihat dokumentasi Flask tentang template: https://flask.palletsprojects.com/en/latest/templating/
