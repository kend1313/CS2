from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("contact.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route("/home")
def contact():
  return render_template("home.html")


@app.route('/skins/<int:id>')
def skin(id):
  conn = sqlite3.connect('CS2.db')
  cur = conn.cursor()
#skin
def case(id):
  conn= sqlite3.connect('CS2.db')
  cur = conn.cursor()
  
  cur.execute('SELECT * FROM Skins WHERE id=?',(id,))
  pizza = cur.fetchone()
# bases
  cur.execute('SELECT * FROM Base WHERE id=?',(id,))
  base = cur.fetchone()
# cur.execute("SELECT toppingname FROM Topping WHERE id = (SELECT tid FROM Pizzatopping WHERE pid= ?)",(id,))
#topping = cur.fetchall()
  return render_template('allskins.html',All_skins, base=base)

if __name__ == "__main__":
    app.run(debug = True)