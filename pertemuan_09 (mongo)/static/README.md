# Static Folder

Folder ini berisi file static (CSS, JavaScript, images) untuk aplikasi CRUD dengan MongoDB.

## 📁 File Static

- **style.css** - Custom stylesheet untuk aplikasi

## 🎨 CSS

File `style.css` berisi custom styling yang melengkapi Bootstrap untuk:
- Custom colors dan themes
- Layout adjustments
- Component styling
- Responsive design tweaks

## 🔗 Cara Menggunakan

File static diakses melalui URL path `/static/`:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

Atau langsung:

```html
<link rel="stylesheet" href="/static/style.css">
```

## 📚 Referensi

Lihat dokumentasi Flask tentang static files: https://flask.palletsprojects.com/en/latest/tutorial/static/
