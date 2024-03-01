from flask import Flask, render_template
import pymysql
from dotenv import load_dotenv
import os
from database.database import init_db


env_path = '.env'
load_dotenv(dotenv_path=env_path)
app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_DATABASE = os.getenv('DB_DATABASE')
db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_DATABASE)


@app.route('/')
def hello() -> None:
    return render_template('index.html')


if __name__ == "__main__":
    init_db(db)
    app.run(host="localhost", port=8080)
