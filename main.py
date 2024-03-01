from flask import Flask, render_template
import pymysql
from dotenv import load_dotenv
import os
from database.database import init_db, select_all_users, select_all_users_payments


env_path = '.env'
load_dotenv(dotenv_path=env_path)
app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_DATABASE = os.getenv('DB_DATABASE')
db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_DATABASE)


@app.route('/')
def main() -> str:
    users = select_all_users_payments(db)
    return render_template('index.html', users=users)


@app.route('/users/')
def users() -> str:
    users = select_all_users(db)
    return render_template('users.html', users=users)


if __name__ == "__main__":
    init_db(db)
    select_all_users(db)
    app.run(host="localhost", port=8080)
