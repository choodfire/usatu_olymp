from flask import Flask, render_template, request, redirect, Response
import pymysql
from dotenv import load_dotenv
import os

from database.database import init_db, select_all_users, select_all_users_payments, add_user_db, change_user_db


env_path = '.env'
load_dotenv(dotenv_path=env_path)
app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_DATABASE = os.getenv('DB_DATABASE')
db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_DATABASE)


@app.route('/', methods=['GET'])
def main() -> str:
    users = select_all_users_payments(db)
    return render_template('index.html', users=users)


@app.route('/users/', methods=['GET'])
def users() -> str:
    users = select_all_users(db)
    return render_template('users.html', users=users)


@app.route('/add_user/', methods=['POST'])
def add_user() -> Response:
    user_name = request.form['name']
    add_user_db(db, user_name)
    return redirect('/users/', code=302)


@app.route('/change_user/', methods=['POST'])
def change_user() -> Response:
    new_name = request.form['name']
    user_id = request.form['id']
    change_user_db(db, user_id, new_name)
    return redirect('/users/', code=302)


if __name__ == "__main__":
    init_db(db)
    select_all_users(db)
    app.run(host="localhost", port=8080)
