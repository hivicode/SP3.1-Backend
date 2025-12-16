from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

client = MongoClient("mongodb://localhost:27017/")
db = client["perumahan"]
collection = db["rumah"]

try:
    collection.create_index("kode_rumah", unique=True)
except Exception:
    pass

@app.route('/')
def index():
    rumah_list = list(collection.find())
    return render_template('index.html', rumah_list=rumah_list)

@app.route('/add', methods=['GET', 'POST'])
def add():
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

        filename = None
        file = request.files.get('file')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        collection.insert_one({
            "kode_rumah": kode_rumah,
            "nama_rumah": nama_rumah,
            "alamat": alamat,
            "harga": int(harga),
            "luas_tanah": int(luas_tanah),
            "luas_bangunan": int(luas_bangunan),
            "kamar_tidur": int(kamar_tidur),
            "kamar_mandi": int(kamar_mandi),
            "developer": developer,
            "filename": filename
        })

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    item = collection.find_one({"_id": ObjectId(id)})

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

        update_data = {
            "nama_rumah": nama_rumah,
            "alamat": alamat,
            "harga": int(harga),
            "luas_tanah": int(luas_tanah),
            "luas_bangunan": int(luas_bangunan),
            "kamar_tidur": int(kamar_tidur),
            "kamar_mandi": int(kamar_mandi),
            "developer": developer
        }

        file = request.files.get('file')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            update_data["filename"] = filename

        collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_data}
        )

        return redirect(url_for('index'))

    return render_template('edit.html', item=item)


@app.route('/delete/<id>')
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
