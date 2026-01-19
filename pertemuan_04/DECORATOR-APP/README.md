# Decorator App

Aplikasi Flask dengan implementasi custom decorator untuk autentikasi dan proteksi halaman.

## 📋 Deskripsi

Aplikasi web yang mendemonstrasikan penggunaan custom decorator untuk proteksi halaman dengan sistem login. Halaman dashboard hanya bisa diakses setelah user login.

## 🚀 Fitur

- **Login System** - Halaman login dengan username dan password
- **Custom Decorator** - `@login_required` untuk proteksi halaman
- **Session Management** - Menggunakan Flask session untuk state management
- **Protected Routes** - Dashboard hanya bisa diakses setelah login
- **Logout Functionality** - Logout dan clear session

## 📁 File

- `decorator_app.py` - Aplikasi Flask utama dengan custom decorator
- `login.html` - Halaman login
- `dashboard.html` - Halaman dashboard (protected)

## 📦 Instalasi

```bash
pip install flask
```

## 🚀 Menjalankan Aplikasi

```bash
python decorator_app.py
```

Akses di browser: `http://127.0.0.1:5001`

**Catatan:** Aplikasi ini menggunakan port 5001 (bukan 5000 default)

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

**Behavior:**
- Jika sudah login: Menampilkan dashboard
- Jika belum login: Redirect ke `/login`

### GET /logout
Logout dan clear session, kemudian redirect ke login.

## 💡 Konsep yang Dipelajari

✅ Custom decorator dengan Python  
✅ Decorator untuk authentication  
✅ Session management dengan Flask  
✅ Protected routes  
✅ Redirect untuk unauthorized access  
✅ Form handling dengan POST method  
✅ Error handling pada login  

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

Decorator ini:
- Memeriksa apakah user sudah login (ada di session)
- Jika belum login, redirect ke halaman login
- Jika sudah login, jalankan function yang di-protect

## 📝 Cara Menggunakan

1. **Akses Aplikasi**
   - Buka `http://localhost:5001`
   - Akan redirect ke halaman login

2. **Login**
   - Masukkan username: `admin`
   - Masukkan password: `admin`
   - Klik tombol Login

3. **Akses Dashboard**
   - Setelah login, akan redirect ke dashboard
   - Dashboard menampilkan welcome message

4. **Logout**
   - Klik tombol Logout
   - Session akan di-clear
   - Redirect kembali ke login

5. **Coba Akses Dashboard Tanpa Login**
   - Setelah logout, coba akses `/dashboard` langsung
   - Akan redirect ke login (karena protected)

## 🛠️ Teknologi

- **Flask** - Web framework
- **Jinja2** - Template engine
- **Session** - State management
- **functools.wraps** - Preserve function metadata

## ⚠️ Catatan Penting

- Port yang digunakan: **5001** (bukan 5000)
- Secret key: `'password'` (ganti untuk production!)
- Credentials hardcoded (untuk production, gunakan database)
- Tidak ada password hashing (untuk production, gunakan bcrypt)

## 🔐 Keamanan

### Untuk Development (Saat Ini)
- ✅ Session management
- ✅ Protected routes dengan decorator
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

1. Memahami konsep decorator di Python
2. Membuat custom decorator untuk authentication
3. Session management dengan Flask
4. Proteksi halaman dengan decorator
5. Redirect untuk unauthorized access
6. Form handling dengan POST method

## 🔧 Tips

- Gunakan `functools.wraps` untuk preserve function metadata
- Periksa session cookie di browser DevTools
- Test akses protected route tanpa login
- Untuk production, gunakan Flask-Login extension

## 📚 Pengembangan Lebih Lanjut

Untuk meningkatkan aplikasi ini:
- Implementasi database untuk user management
- Gunakan Flask-Login extension
- Tambahkan password hashing
- Implementasi registration form
- Tambahkan role-based access control
- Implementasi "Remember Me" functionality
- Tambahkan CSRF protection