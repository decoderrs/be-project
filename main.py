import json

from flask import Flask, render_template, jsonify
import os
import mysql.connector
import requests

from Controller.graphPlot import graphPlot
from Controller.newsdb import newsDb

app = Flask(__name__, template_folder=os.path.abspath('templates'), static_folder=os.path.abspath('static'))

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/charts", methods=['GET', 'POST'])
def event():
    server_ip = 'http://127.0.0.1:8001/charts'
    headers = {'Content-Type': 'application/json'}
    event_data = {'data_1': 75, 'data_2': -1, 'data_3': 47, 'data_4': 'SBY'}
    server_return = requests.post(server_ip, headers=headers, json=jsonify(event_data))
    print(server_return.json())
    return server_return.json()


@app.route("/home")
def home():
    print(cursor.rowcount, "record inserted.")
    newsdb.delete_news()
    newsdb.create()
    context = {
        "s_data": newsdb.read_news()
    }
    return render_template("homePage.html", **context)


@app.route("/static/<s_name>")
def charts(s_name):
    context = {
        "s_data": newsdb.read_news()
    }
    return render_template("charts.html", **context)


if __name__ == "__main__":
    gp = graphPlot()
    # gp.createGraph()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",
        database="BE",
        autocommit=True
    )
    

    cursor = mydb.cursor()
    newsdb = newsDb(cursor, mydb)

    app.run(debug=True, port=8001)
