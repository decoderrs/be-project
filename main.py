from flask import Flask, render_template
import os
import sqlite3

app = Flask(__name__, template_folder=os.path.abspath('templates'), static_folder=os.path.abspath('static'))
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine", "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Fritz", "score": 92},
    {"name": "Frieda", "score": 40},
    {"name": "Sirius", "score": 75}
]

username = [
    {"name": "home"},
    {"name": "about"},
    {"name": "contactus"},
    {"name": "charts"}
]
stocks = [
    {"stock_name": "RELIANCE" , "volume": 12000, "diff": round(2300/12000 , 2), "trend": True},
    {"stock_name": "HDFCBANK", "volume": 12000, "diff": (2300/12000), "trend": False},
    {"stock_name": "ADANIENT", "volume": 12000, "diff": (2300/12000), "trend": True},
    {"stock_name": "ICICIBANK", "volume": 12000, "diff": (2300/12000), "trend": False},
    {"stock_name": "SBIN", "volume": 12000, "diff": (2300/12000), "trend": True}
]


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/index')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route("/home")
def home():
    context = {
        "username": username,
        "stocks": stocks
    }
    return render_template("homePage.html", **context)


@app.route("/home/<uname>")
def test(uname):
    context = {
        "username": username,
        "uname": uname
    }
    return render_template("test.html",**context)


@app.route("/results")
def results():
    context = {
        "title": "Results",
        "students": students,
        "test_name": test_name,
        "max_score": max_score,
    }
    return render_template("results.html", **context)


@app.route("/home/charts/<s_name>")
def charts(s_name):
    context = {
        "username": username,
        "stocks": stocks,
        "s_name": s_name
    }
    return render_template("charts.html",**context)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
