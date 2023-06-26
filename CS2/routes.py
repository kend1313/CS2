from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("home.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route ("/all_skins")

def all_skins():
  conn=sqlite3.connect("CS2.db")
  cur=conn.cursor()
  cur.execute('SELECT * FROM skins')
  results=cur.fetchall()
  conn.close
  return render_template("allskins.html",results = results)

@app.route('/skins/<int:id>')
def pizza(id):
  conn = sqlite3.connect('CS2.db')
  cur = conn.cursor()
#pizza
  cur.execute('SELECT * FROM Skins WHERE id=?',(id,))
  pizza = cur.fetchone()
# base
  cur.execute('SELECT * FROM Base WHERE id=?',(id,))
  base = cur.fetchone()
# cur.execute("SELECT toppingname FROM Topping WHERE id = (SELECT tid FROM Pizzatopping WHERE pid= ?)",(id,))
#topping = cur.fetchall()
  return render_template('Skin.html',all_skins = all_skins,base = base)

if __name__ == "__main__":
    app.run(debug = True)

