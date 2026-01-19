# Routing App

Aplikasi Flask yang mendemonstrasikan routing dasar dan rendering template HTML.

## 📋 Deskripsi

Aplikasi web sederhana dengan multiple routes dan template HTML. Aplikasi ini menunjukkan cara membuat routing di Flask dan merender template HTML menggunakan Jinja2.

## 🚀 Fitur

- **Multiple Routes** - Beberapa halaman dengan route berbeda
- **Template Rendering** - Menggunakan Jinja2 template engine
- **Static HTML Pages** - Halaman HTML sederhana
- **Navigation** - Link antar halaman

## 📁 File

- `routing_app.py` - Aplikasi Flask utama
- `index.html` - Halaman utama
- `about.html` - Halaman tentang
- `contact.html` - Halaman kontak
- `form.html` - Halaman form

## 📦 Instalasi

```bash
pip install flask
```

## 🚀 Menjalankan Aplikasi

```bash
python routing_app.py
```

Akses di browser: `http://127.0.0.1:5000`

## 🔌 Routes

### GET /
Halaman utama/homepage.

**Template:** `index.html`

### GET /about
Halaman tentang (About page).

**Template:** `about.html`

### GET /contact
Halaman kontak (Contact page).

**Template:** `contact.html`

### GET /form
Halaman form (Form page).

**Template:** `form.html`

## 💡 Konsep yang Dipelajari

✅ Routing dasar dengan Flask  
✅ Template rendering dengan `render_template()`  
✅ Multiple routes dalam satu aplikasi  
✅ Jinja2 template engine  
✅ Static HTML pages  
✅ Navigation antar halaman  

## 📝 Cara Menggunakan

1. **Jalankan Aplikasi**
   ```bash
   python routing_app.py
   ```

2. **Akses di Browser**
   - Homepage: `http://localhost:5000/`
   - About: `http://localhost:5000/about`
   - Contact: `http://localhost:5000/contact`
   - Form: `http://localhost:5000/form`

3. **Navigasi**
   - Gunakan link di setiap halaman untuk berpindah
   - Atau ketik URL langsung di browser

## 🛠️ Teknologi

- **Flask** - Web framework
- **Jinja2** - Template engine
- **HTML** - Markup language

## 📚 Struktur Template

Template HTML disimpan di folder yang sama dengan `routing_app.py` (bukan di folder `templates/`).

Konfigurasi di `routing_app.py`:
```python
app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))
```

## 🎯 Tujuan Pembelajaran

1. Memahami konsep routing di Flask
2. Membuat multiple routes
3. Template rendering dengan Jinja2
4. Struktur aplikasi Flask sederhana
5. Navigation antar halaman

## 🔧 Tips

- Template bisa disimpan di folder `templates/` (default) atau folder custom
- Gunakan `url_for()` untuk generate URL secara dinamis
- Template bisa menggunakan inheritance dengan `extends` dan `block`
- Untuk production, gunakan folder `templates/` yang terpisah

## 📊 Struktur Routing

```
/          → index.html (Homepage)
/about     → about.html (About page)
/contact   → contact.html (Contact page)
/form      → form.html (Form page)
```

## 🔄 Perbandingan dengan Folder Templates

| Aspek | Routing App | Standard Flask |
|-------|-------------|----------------|
| Template Location | Same folder as app.py | `templates/` folder |
| Configuration | Custom `template_folder` | Default |
| Use Case | Simple apps | Production apps |

## 📝 Catatan

- Template disimpan di folder yang sama dengan aplikasi
- Ini adalah contoh sederhana, untuk aplikasi yang lebih kompleks gunakan folder `templates/`
- Setiap route merender template HTML yang berbeda