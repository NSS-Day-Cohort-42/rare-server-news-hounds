import sqlite3
import json
from models import Comment, User, Post

# get_all_comments, #get_comments_by_post_id, #get_single_comment

def create_comment(comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO comment
            (content, timestamp, post_id, user_id)
        VALUES (?, ?, ?, ?)
        """, (comment['content'], comment['timestamp'], comment['post_id'], comment['user_id'], ))
        id = db_cursor.lastrowid
        comment['id'] = id
    return json.dumps(comment)