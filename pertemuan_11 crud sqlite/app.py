from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret123"

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "perumahan.db")
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.template_filter("currency")
def currency_filter(value):
    return "{:,.0f}".format(value)


def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS rumah (
            kode_rumah TEXT PRIMARY KEY,
            nama_rumah TEXT NOT NULL,
            alamat TEXT NOT NULL,
            harga INTEGER NOT NULL,
            luas_tanah INTEGER NOT NULL,
            luas_bangunan INTEGER NOT NULL,
            kamar_tidur INTEGER NOT NULL,
            kamar_mandi INTEGER NOT NULL,
            developer TEXT NOT NULL,
            filename TEXT
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    search_query = request.args.get("search", "")
    page = int(request.args.get("page", 1))
    per_page = 5
    offset = (page - 1) * per_page

    conn = get_db()
    cur = conn.cursor()

    if search_query:
        like_q = f"%{search_query}%"
        cur.execute(
            "SELECT COUNT(*) FROM rumah WHERE nama_rumah LIKE ? OR alamat LIKE ?",
            (like_q, like_q),
        )
    else:
        cur.execute("SELECT COUNT(*) FROM rumah")
    total_rows = cur.fetchone()[0]
    total_pages = (total_rows + per_page - 1) // per_page if total_rows > 0 else 1

    if search_query:
        like_q = f"%{search_query}%"
        cur.execute(
            """
            SELECT * FROM rumah
            WHERE nama_rumah LIKE ? OR alamat LIKE ?
            LIMIT ? OFFSET ?
            """,
            (like_q, like_q, per_page, offset),
        )
    else:
        cur.execute("SELECT * FROM rumah LIMIT ? OFFSET ?", (per_page, offset))

    rows = cur.fetchall()
    conn.close()

    rumah_list = rows

    return render_template(
        "index.html",
        rumah_list=rumah_list,
        page=page,
        total_pages=total_pages,
        search_query=search_query,
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/add", methods=["GET", "POST"])
def add_rumah():
    if request.method == "POST":
        kode_rumah = request.form["kode_rumah"]
        nama_rumah = request.form["nama_rumah"]
        alamat = request.form["alamat"]
        harga = request.form["harga"]
        luas_tanah = request.form["luas_tanah"]
        luas_bangunan = request.form["luas_bangunan"]
        kamar_tidur = request.form["kamar_tidur"]
        kamar_mandi = request.form["kamar_mandi"]
        developer = request.form["developer"]
        file = request.files.get("file")

        filename = None
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO rumah (
                kode_rumah, nama_rumah, alamat, harga,
                luas_tanah, luas_bangunan, kamar_tidur, kamar_mandi,
                developer, filename
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                kode_rumah,
                nama_rumah,
                alamat,
                harga,
                luas_tanah,
                luas_bangunan,
                kamar_tidur,
                kamar_mandi,
                developer,
                filename,
            ),
        )
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_rumah(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM rumah WHERE kode_rumah = ?", (id,))
    rumah_data = cur.fetchone()

    if request.method == "POST":
        if rumah_data and rumah_data["filename"]:
            old_file = rumah_data["filename"]
            old_path = os.path.join(app.config["UPLOAD_FOLDER"], old_file)
            if os.path.exists(old_path):
                os.remove(old_path)

        kode_rumah = request.form["kode_rumah"]
        nama_rumah = request.form["nama_rumah"]
        alamat = request.form["alamat"]
        harga = request.form["harga"]
        luas_tanah = request.form["luas_tanah"]
        luas_bangunan = request.form["luas_bangunan"]
        kamar_tidur = request.form["kamar_tidur"]
        kamar_mandi = request.form["kamar_mandi"]
        developer = request.form["developer"]
        new_file = request.files.get("file")

        filename = rumah_data["filename"] if rumah_data else None
        if new_file and new_file.filename and allowed_file(new_file.filename):
            filename = secure_filename(new_file.filename)
            new_file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        cur.execute(
            """
            UPDATE rumah SET
                kode_rumah = ?,
                nama_rumah = ?,
                alamat = ?,
                harga = ?,
                luas_tanah = ?,
                luas_bangunan = ?,
                kamar_tidur = ?,
                kamar_mandi = ?,
                developer = ?,
                filename = ?
            WHERE kode_rumah = ?
            """,
            (
                kode_rumah,
                nama_rumah,
                alamat,
                harga,
                luas_tanah,
                luas_bangunan,
                kamar_tidur,
                kamar_mandi,
                developer,
                filename,
                id,
            ),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    conn.close()
    return render_template("edit.html", rumah_data=rumah_data)


@app.route("/delete/<id>")
def delete_rumah(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT filename FROM rumah WHERE kode_rumah = ?", (id,))
    file_data = cur.fetchone()
    if file_data and file_data["filename"]:
        file = file_data["filename"]
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file)
        if os.path.exists(file_path):
            os.remove(file_path)
    cur.execute("DELETE FROM rumah WHERE kode_rumah = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)