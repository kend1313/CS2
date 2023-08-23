from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/all_skins")
def all_skins():
    conn = sqlite3.connect("CS2.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM skin')
    results = cur.fetchall()
    conn.close()
    return render_template("allskins.html", results=results)


@app.route('/skin/<int:id>')
def skin(id):
    conn = sqlite3.connect('CS2.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM skin WHERE id=?', (id,))
    description = cur.fetchone()
    return render_template('skin.html', description=description)


if __name__ == "__main__":
    app.run(debug=True)
