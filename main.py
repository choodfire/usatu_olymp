from flask import Flask, render_template
import pymysql

app = Flask(__name__)
db = pymysql.connect(host="localhost", user="root", password="pass", database="db")


@app.route('/')
def hello():
    return render_template('index.html')
