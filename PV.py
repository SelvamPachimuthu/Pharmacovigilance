from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cases(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient TEXT,
        drug TEXT,
        reaction TEXT
    )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    patient = request.form["patient"]
    drug = request.form["drug"]
    reaction = request.form["reaction"]

    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO cases(patient,drug,reaction) VALUES(?,?,?)",
                (patient, drug, reaction))
    conn.commit()
    conn.close()

    return "Case Saved Successfully"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)