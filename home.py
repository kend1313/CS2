from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
# display the home page, connect with home.html

@app.route('/about')
def about():
    return render_template("about.html")
# display the about page, connect with home.html


@app.route("/contact")
def contact():
    return render_template("contact.html")
# display the contact page, connect with home.html


@app.route("/all_skins")
def all_skins():
    conn = sqlite3.connect("CS2.db")
# connect with the database
    cur = conn.cursor()
# opening the warehouse
    cur.execute('SELECT * FROM skin')
# Select the id from database
    results = cur.fetchall()
# print result(s)
    conn.close()
    return render_template("allskins.html", results=results)
# display on allskins.html page with name results

@app.route('/skin/<int:id>')
def skin(id):
    conn = sqlite3.connect('CS2.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM skin WHERE id=?', (id,))
    description = cur.fetchone()
# print the single reult for skin
    cur.execute('SELECT * FROM CaseBelong WHERE id=?',(id,))
    CaseBelong = cur.fetchone()
# print the single result for CaseBelong
    cur.execute('SELECT * FROM ItemQuality WHERE id=?',(id,))
    ItemQuality = cur.fetchone()
# print the single result for ItemQuality
    return render_template('skin.html', description=description,
    CaseBelong=CaseBelong, ItemQuality=ItemQuality)

if __name__ == "__main__":
    app.run(debug=True)
