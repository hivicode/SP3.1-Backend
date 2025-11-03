from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_mysqldb import MySQL
import os
import math
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'secret123'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'uts_rumah_db'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

mysql = MySQL(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    search_query = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = 5
    offset = (page - 1) * per_page
    
    cur = mysql.connection.cursor()
    
    if search_query:
        cur.execute("SELECT COUNT(*) FROM rumah WHERE nama_rumah LIKE %s OR alamat LIKE %s", ('%' + search_query + '%', '%' + search_query + '%'))
    else:
        cur.execute("SELECT COUNT(*) FROM rumah")
    total_rows = cur.fetchone()[0]
    total_pages = math.ceil(total_rows / per_page) if total_rows > 0 else 1
    
    if search_query:
        cur.execute("""
            SELECT * FROM rumah
            WHERE nama_rumah LIKE %s OR alamat LIKE %s
            LIMIT %s OFFSET %s
        """, ('%' + search_query + '%', '%' + search_query + '%', per_page, offset))
    else:
        cur.execute("SELECT * FROM rumah LIMIT %s OFFSET %s", (per_page, offset))
    
    rumah_list = cur.fetchall()
    cur.close()
    
    return render_template('index.html', rumah_list=rumah_list, page=page, 
                         total_pages=total_pages, search_query=search_query)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/add', methods=['GET','POST'])
def add_rumah():
    if request.method == 'POST':
        kode_rumah = request.form['kode_rumah']
        nama_rumah = request.form['nama_rumah']
        alamat = request.form['alamat']
        harga = request.form['harga']
        luas_tanah = request.form['luas_tanah']
        luas_bangunan = request.form['luas_bangunan']
        kamar_tidur = request.form['kamar_tidur']
        kamar_mandi = request.form['kamar_mandi']
        developer = request.form['developer']
        file = request.files.get('file')

        filename = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO rumah (kode_rumah, nama_rumah, alamat, harga, luas_tanah, luas_bangunan, kamar_tidur, kamar_mandi, developer, filename) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (kode_rumah, nama_rumah, alamat, harga, luas_tanah, luas_bangunan, kamar_tidur, kamar_mandi, developer, filename))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET','POST'])
def edit_rumah(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rumah WHERE kode_rumah = %s", (id,))
    rumah_data = cur.fetchone()

    if request.method == 'POST':
        if rumah_data and rumah_data[9]:
            old_file = rumah_data[9]
            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], old_file)):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], old_file))

        kode_rumah = request.form['kode_rumah']
        nama_rumah = request.form['nama_rumah']
        alamat = request.form['alamat']
        harga = request.form['harga']
        luas_tanah = request.form['luas_tanah']
        luas_bangunan = request.form['luas_bangunan']
        kamar_tidur = request.form['kamar_tidur']
        kamar_mandi = request.form['kamar_mandi']
        developer = request.form['developer']
        new_file = request.files.get('file')

        if new_file and allowed_file(new_file.filename):
            filename = secure_filename(new_file.filename)
            new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cur.execute("""
                UPDATE rumah SET kode_rumah = %s, nama_rumah = %s, alamat = %s, harga = %s, 
                luas_tanah = %s, luas_bangunan = %s, kamar_tidur = %s, kamar_mandi = %s, 
                developer = %s, filename = %s WHERE kode_rumah = %s
            """, (kode_rumah, nama_rumah, alamat, harga, luas_tanah, luas_bangunan, kamar_tidur, kamar_mandi, developer, filename, id))
        else:
            cur.execute("""
                UPDATE rumah SET kode_rumah = %s, nama_rumah = %s, alamat = %s, harga = %s, 
                luas_tanah = %s, luas_bangunan = %s, kamar_tidur = %s, kamar_mandi = %s, 
                developer = %s WHERE kode_rumah = %s
            """, (kode_rumah, nama_rumah, alamat, harga, luas_tanah, luas_bangunan, kamar_tidur, kamar_mandi, developer, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

    cur.close()
    return render_template('edit.html', rumah_data=rumah_data)

@app.route('/delete/<id>')
def delete_rumah(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT filename FROM rumah WHERE kode_rumah = %s", (id,))
    file_data = cur.fetchone()
    if file_data and file_data[0]:
        file = file_data[0]
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], file)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file))
    cur.execute("DELETE FROM rumah WHERE kode_rumah = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

