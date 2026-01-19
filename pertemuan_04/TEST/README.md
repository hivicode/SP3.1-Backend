# Test - Routing dan Login App

Aplikasi Flask yang menggabungkan routing dengan sistem login authentication lengkap.

## 📋 Deskripsi

Aplikasi testing yang menggabungkan konsep routing dengan sistem login. Aplikasi ini memiliki multiple protected pages yang memerlukan autentikasi sebelum bisa diakses.

## 🚀 Fitur

- **Multiple Routes** - Beberapa halaman (home, about, contact, dashboard)
- **Login System** - Halaman login dengan username dan password
- **Protected Pages** - Multiple pages yang memerlukan login
- **Session Management** - Menggunakan Flask session
- **Custom Decorator** - `@login_required` untuk proteksi halaman
- **Logout Functionality** - Logout dan clear session

## 📁 File

- `routing_login_app.py` - Aplikasi Flask utama
- `index.html` - Halaman utama (redirect ke login)
- `about.html` - Halaman tentang (protected)
- `contact.html` - Halaman kontak (protected)
- `login.html` - Halaman login
- `dashboard.html` - Halaman dashboard (protected)

## 📦 Instalasi

```bash
pip install flask
```

## 🚀 Menjalankan Aplikasi

```bash
python routing_login_app.py
```

Akses di browser: `http://127.0.0.1:5002`

**Catatan:** Aplikasi ini menggunakan port 5002 (bukan 5000 default)

## 🔐 Login Credentials

Default credentials:
- **Username**: `admin`
- **Password**: `admin`

⚠️ **PENTING**: Ganti credentials ini untuk production!

## 🔌 Routes

### GET /
Redirect ke halaman login.

### GET /login
Menampilkan halaman login.

### POST /login
Proses login dengan validasi credentials.

**Request Body:**
```
username=admin&password=admin
```

**Response:**
- Jika berhasil: Redirect ke `/dashboard`
- Jika gagal: Kembali ke `/login` dengan error message

### GET /dashboard
Halaman dashboard (protected - memerlukan login).

### GET /about
Halaman tentang (protected - memerlukan login).

### GET /contact
Halaman kontak (protected - memerlukan login).

### GET /logout
Logout dan clear session, kemudian redirect ke login.

## 💡 Konsep yang Dipelajari

✅ Routing dengan multiple pages  
✅ Login authentication  
✅ Custom decorator untuk proteksi  
✅ Session management  
✅ Multiple protected routes  
✅ Error handling pada login  
✅ Logout functionality  
✅ Redirect untuk unauthorized access  

## 🎯 Custom Decorator

Aplikasi menggunakan custom decorator `@login_required`:

```python
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
```

Semua protected routes menggunakan decorator ini:
- `/dashboard` - Protected
- `/about` - Protected
- `/contact` - Protected

## 📝 Cara Menggunakan

1. **Akses Aplikasi**
   - Buka `http://localhost:5002`
   - Akan redirect ke halaman login

2. **Login**
   - Masukkan username: `admin`
   - Masukkan password: `admin`
   - Klik tombol Login

3. **Akses Protected Pages**
   - Setelah login, bisa akses:
     - Dashboard: `/dashboard`
     - About: `/about`
     - Contact: `/contact`

4. **Navigasi**
   - Gunakan menu/link untuk berpindah antar halaman
   - Semua halaman protected bisa diakses setelah login

5. **Logout**
   - Klik tombol Logout
   - Session akan di-clear
   - Redirect kembali ke login

6. **Coba Akses Tanpa Login**
   - Setelah logout, coba akses protected pages
   - Akan redirect ke login

## 🛠️ Teknologi

- **Flask** - Web framework
- **Jinja2** - Template engine
- **Session** - State management
- **functools.wraps** - Preserve function metadata

## ⚠️ Catatan Penting

- Port yang digunakan: **5002** (bukan 5000)
- Secret key: `'password'` (ganti untuk production!)
- Credentials hardcoded (untuk production, gunakan database)
- Tidak ada password hashing (untuk production, gunakan bcrypt)
- Multiple protected pages dengan decorator yang sama

## 🔐 Keamanan

### Untuk Development (Saat Ini)
- ✅ Session management
- ✅ Protected routes dengan decorator
- ✅ Multiple protected pages
- ⚠️ Password tidak di-hash
- ⚠️ Credentials hardcoded
- ⚠️ Secret key tidak aman

### Untuk Production
- ✅ Gunakan password hashing (bcrypt, werkzeug.security)
- ✅ Simpan credentials di database
- ✅ Gunakan secret key yang kuat (random string)
- ✅ Implementasi CSRF protection
- ✅ Rate limiting untuk login attempts
- ✅ Session timeout

## 🎯 Tujuan Pembelajaran

1. Menggabungkan routing dengan authentication
2. Multiple protected pages dengan satu decorator
3. Session management untuk state
4. Navigation antar protected pages
5. Logout functionality
6. Error handling pada login

## 🔧 Tips

- Gunakan `functools.wraps` untuk preserve function metadata
- Periksa session cookie di browser DevTools
- Test akses semua protected routes tanpa login
- Untuk production, gunakan Flask-Login extension

## 📊 Struktur Routes

```
/           → Redirect ke /login
/login      → Login page (GET & POST)
/dashboard  → Dashboard (protected)
/about      → About page (protected)
/contact    → Contact page (protected)
/logout     → Logout
```

## 🔄 Perbandingan dengan Aplikasi Lain

| Aspek | Routing App | Decorator App | Test App |
|-------|-------------|---------------|----------|
| Routes | Multiple | Few | Multiple |
| Login | ❌ | ✅ | ✅ |
| Protected Pages | ❌ | 1 (dashboard) | 3 (dashboard, about, contact) |
| Port | 5000 | 5001 | 5002 |

## 📚 Pengembangan Lebih Lanjut

Untuk meningkatkan aplikasi ini:
- Implementasi database untuk user management
- Gunakan Flask-Login extension
- Tambahkan password hashing
- Implementasi registration form
- Tambahkan role-based access control
- Implementasi "Remember Me" functionality
- Tambahkan CSRF protection
- Tambahkan more protected pages