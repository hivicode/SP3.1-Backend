# Templates Folder

Folder ini berisi file template HTML untuk aplikasi CRUD dengan MongoDB dan fitur upload file.

## 📁 File Template

- **index.html** - Halaman utama untuk menampilkan daftar data rumah dengan gambar
- **add.html** - Form untuk menambah data rumah baru dengan upload foto
- **edit.html** - Form untuk mengedit data rumah dan update foto

## 🎨 Template Engine

Template menggunakan **Jinja2** yang merupakan template engine default Flask.

## 📝 Fitur Template

- Bootstrap 5.3.0 untuk styling
- Form handling dengan Flask (multipart/form-data untuk upload)
- Dynamic content rendering dengan gambar rumah
- Image preview dan display
- Responsive design
- Error message display

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
    rumah = collection.find()
    return render_template('index.html', rumah=rumah)
```

## 📚 Referensi

Lihat dokumentasi Flask tentang template: https://flask.palletsprojects.com/en/latest/templating/
