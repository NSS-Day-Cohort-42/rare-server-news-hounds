import sqlite3
import json
from models import User

def get_all_users():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.username,
            u.email,
            u.password
        FROM User u
        """)
        
        users = []
        
        dataset = db_cursor.fetchall()
       
        for row in dataset:
            user = User(row['id'], row['first_name'], row['last_name'], row['username'],
                    row['email'], row['password'])

            users.append(user.__dict__)

            
    return json.dumps(users)


def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO User
            ( first_name, last_name, username, email, password )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_user['first_name'], new_user['last_name'],
              new_user['username'], new_user['email'],
              new_user['password'], ))
        
        id = db_cursor.lastrowid
        
        new_user['id'] = id

    return json.dumps(new_user)

def get_single_user(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.username,
            u.email,
            u.password
        FROM User u
        WHERE u.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()
        
        if data:
            user = User(data['id'], data['first_name'], data['last_name'], data['username'],
                        data['email'], data['password'])
        
            return json.dumps(user.__dict__)
        else:
            return False