# Pertemuan 4 - Routing dan Authentication

Materi pembelajaran sistem routing dan autentikasi dalam Flask.

## 📚 Daftar Materi

### 1. ROUTING-APP
Implementasi routing dasar dengan template HTML.

### 2. DECORATOR-APP
Penggunaan decorator untuk autentikasi dan proteksi halaman.

### 3. ROUTING_LOGIN
Sistem routing lengkap dengan login, session management, dan multiple protected pages.

## 🚀 Cara Menjalankan

### ROUTING-APP (Basic Routing)

```bash
cd ROUTING-APP
python routing_app.py
```

**Routes:**
- `/` - Homepage (index.html)
- `/about` - About page
- `/contact` - Contact page

**Akses di browser:**
```
http://localhost:5000/
http://localhost:5000/about
http://localhost:5000/contact
```

**File yang digunakan:**
- `routing_app.py` - Aplikasi Flask
- `index.html` - Halaman utama
- `about.html` - Halaman about
- `contact.html` - Halaman contact

---

### DECORATOR-APP (Login dengan Decorator)

```bash
cd DECORATOR-APP
python decorator_app.py
```

**Routes:**
- `/` - Redirect ke login
- `/login` - Halaman login (GET & POST)
- `/dashboard` - Dashboard (protected)
- `/logout` - Logout

**Login Credentials:**
- Username: `admin`
- Password: `admin`

**Akses di browser:**
```
http://localhost:5001/login
```

**File yang digunakan:**
- `decorator_app.py` - Aplikasi Flask dengan decorator
- `login.html` - Halaman login
- `dashboard.html` - Halaman dashboard

**Fitur:**
- Custom decorator `@login_required`
- Session management
- Protected routes
- Redirect untuk unauthorized access

---

### ROUTING_LOGIN (Complete Auth System)

```bash
cd ROUTING_LOGIN
python routing_login_app.py
```

**Routes:**
- `/` - Redirect ke login
- `/login` - Halaman login (GET & POST)
- `/dashboard` - Dashboard (protected)
- `/about` - About page (protected)
- `/contact` - Contact page (protected)
- `/logout` - Logout

**Login Credentials:**
- Username: `admin`
- Password: `admin`

**Akses di browser:**
```
http://localhost:5002/login
```

**File yang digunakan:**
- `routing_login_app.py` - Aplikasi Flask lengkap
- `login.html` - Halaman login
- `dashboard.html` - Halaman dashboard
- `about.html` - Halaman about
- `contact.html` - Halaman contact

**Fitur:**
- Multiple protected pages
- Session management
- Custom decorator untuk authentication
- Error handling pada login
- Logout functionality

## 💡 Fitur yang Dipelajari

✅ Routing multi-halaman dengan Flask  
✅ Template rendering dengan Jinja2  
✅ Session management  
✅ Custom decorator untuk authentication  
✅ Protected routes dengan `@login_required`  
✅ Login/Logout functionality  
✅ Redirect unauthorized users  
✅ Form handling (POST method)  
✅ Error messages pada login  

## 📝 Catatan Penting

- **ROUTING-APP** menggunakan port `5000`
- **DECORATOR-APP** menggunakan port `5001`
- **ROUTING_LOGIN** menggunakan port `5002`
- Semua menggunakan `secret_key = 'password'` (ganti untuk production!)
- Template folder menggunakan `template_folder=os.path.dirname(os.path.abspath(__file__))`

## 🎯 Tujuan Pembelajaran

1. Memahami sistem routing dalam Flask
2. Implementasi template rendering
3. Membuat sistem autentikasi sederhana
4. Menggunakan session untuk state management
5. Membuat custom decorator
6. Proteksi halaman dengan authentication
7. Handle form submission

## 🔧 Tips & Best Practices

### Keamanan
- ⚠️ Jangan gunakan `secret_key = 'password'` di production
- ⚠️ Simpan secret key di environment variable
- ⚠️ Gunakan password hashing (bcrypt, werkzeug.security)
- ⚠️ Implement CSRF protection untuk production

### Development
- Gunakan `debug=True` hanya untuk development
- Port berbeda untuk menjalankan multiple apps sekaligus
- Periksa session cookie di browser DevTools
- Gunakan `functools.wraps` untuk preserve function metadata

### Testing
- Test login dengan credentials yang benar dan salah
- Test akses protected routes tanpa login
- Test logout functionality
- Periksa redirect behavior

## 🔐 Cara Kerja Decorator

```python
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
```

Decorator ini memeriksa apakah user sudah login (ada di session). Jika belum, redirect ke halaman login. Jika sudah, jalankan function yang di-protect.

## 📚 Pengembangan Lebih Lanjut

Untuk meningkatkan aplikasi ini, Anda bisa:
- Implementasi database untuk user management
- Gunakan Flask-Login extension
- Tambahkan password hashing
- Implementasi registration form
- Tambahkan role-based access control
- Implementasi "Remember Me" functionality
- Tambahkan CSRF protection

