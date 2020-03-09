#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import abort
from flask_cors import CORS

import sqlite3
from sqlite3 import Error, IntegrityError

import json
from collections import namedtuple


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})

db_file = "mobile-app"

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_tables():
    conn = create_connection ()
    sql = 'CREATE TABLE IF NOT EXISTS USER(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar, phone varchar unique, email varchar unique, password varchar)'
    cur = conn.cursor()
    cur.execute(sql)
    sql = 'CREATE TABLE IF NOT EXISTS SCORE(id INTEGER PRIMARY KEY AUTOINCREMENT, highest_score int default 0, attempts int default 0, attempts_remaining int default 0, user_id int, last_update DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(user_id) references USER(id))'
    cur.execute(sql)

create_tables()


def add_user(conn, user):
    try:
        sql = ''' INSERT INTO USER(name,email,phone,password)
                  VALUES(?,?,?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, (user.name, user.email, user.phone, user.password))
        user_id = cur.lastrowid
        print (user_id)
        score = (user_id,)
        sql = '''INSERT INTO SCORE(user_id) VALUES(?)'''
        cur = conn.cursor()
        cur.execute(sql, score)
        return {
            "status": "success",
            "user": get_record(conn, user_id)
        }
    except IntegrityError as e:
        return {
            "status": "error",
            "reason": str(e)
        }

def record_to_dict(record):
    return {
        "id": record[0],
        "name": record[1],
        "phone": record[2],
        "email": record[3],
        "highest_score": record[6],
        "attempts": record[7],
        "attempts_remaining": record[8],
        "last_update": record[10]
    }

def login_user(conn, loginVo):
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER u, SCORE s WHERE u.id = s.user_id and (u.email = ? or u.phone = ?) and u.password = ?", (loginVo.userId, loginVo.userId, loginVo.password, ))
    user = cur.fetchone()
    if user:
        return {
            "status": "success",
            "user": record_to_dict(user)
        }
    else:
        return {
            "status": "error",
            "reason": "Invalid user name or password"
        }

def get_record(conn, id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER u, SCORE s WHERE u.id = s.user_id and u.id = ?", (id,))
    return record_to_dict(cur.fetchone())

def get_all_records(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM USER u, SCORE s WHERE u.id = s.user_id")
 
    rows = cur.fetchall()
    
    records = []

    for row in rows:
        records.append(record_to_dict(row))

    return records

@app.route('/login', methods=['POST'])
def login():
    if not request.json:
        abort(400)
    loginVo = json_to_dict(request.json)
    conn = create_connection()
    with conn:
        return login_user(conn, loginVo)

@app.route('/register', methods=['POST'])
def register():
    if not request.json:
        abort(400)
    user = json_to_dict(request.json)
    conn = create_connection ()
    with conn:
        return jsonify(add_user(conn, user))

@app.route('/score/update', methods=['POST'])
def update_user_score():
    if not request.json:
        abort(400)
    user = json_to_dict(request.json)
    conn = create_connection ()
    with conn:
        return jsonify(update_score(conn, user))

@app.route('/user/<id>')
def get_user_record(id):
    conn = create_connection()
    with conn:
        record = get_record(conn, id)
        record['rank'] = get_rank(conn, id)
        return jsonify(record)

@app.route('/list', methods=['GET'])
def list():
    conn = create_connection()
    with conn:
        return jsonify(get_all_records(conn))

@app.route('/scoreboard', methods=['GET'])
def score_board():
    conn = create_connection()
    with conn:
        return jsonify(create_score_board(conn))

def create_score_board(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM USER u, SCORE s WHERE u.id = s.user_id ORDER BY s.highest_score DESC, s.attempts ASC LIMIT 10')
    records = []
    rank = 1
    for row in cur.fetchall():
        record = record_to_dict(row)
        record['rank'] = rank
        rank += 1
        records.append(record)

    return records

def get_rank(conn, id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM SCORE ORDER BY highest_score DESC, attempts ASC')
    rank = 1
    for row in cur.fetchall():
        if str(row[4]) == id:
            return rank
        rank += 1

def update_score(conn, score):
    cur = conn.cursor()
    cur.execute('UPDATE SCORE SET highest_score = (CASE WHEN highest_score < ? THEN ? ELSE highest_score END), attempts = attempts + 1 WHERE user_id=?',
        (score.highest_score, score.highest_score, score.id))
    return get_record(conn, score.id)


def json_to_dict(data):
    return json.loads(
        json.dumps(data), 
        object_hook=lambda d: namedtuple('X', d.keys())(*d.values())
    )

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
