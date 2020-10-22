from models import category
import sqlite3
import json
from models import Category

def get_all_categories():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.name
        FROM Category c    
        """)
        categories = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            category = Category(row['id'], row['name'])
            categories.append(category.__dict__)

        return json.dumps(categories)    

def get_single_category(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT 
            c.id,
            c.name
        FROM Category c
        WHERE c.id = ?    
        """, (id, ))    
        row = db_cursor.fetchone()
        category = Category(row['id'], row['name'])
        return json.dumps(category.__dict__)

def create_category(category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Category
            (name)
        VALUES
            (?)    
        """, (category['name'],))
        id = db_cursor.lastrowid
        category['id'] = id
    return json.dumps(category)