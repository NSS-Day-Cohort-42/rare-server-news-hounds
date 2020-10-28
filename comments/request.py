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

def get_comments_by_post_id(post_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT 
        c.id, 
        c.content,
        c.timestamp,
        c.post_id,
        c.user_id,
        u.first_name,
        u.last_name,
        u.username
        FROM comment c
        JOIN user u ON u.id = c.user_id
        WHERE c.post_id = ?
        """, (post_id,))
        comments = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            comment = Comment(row['id'], row['content'], row['timestamp'], row['post_id'], row['user_id'])
            comments.append(comment.__dict__)
            user = User(row['user_id'], row['first_name'], row['last_name'], row['username'], "", "")
            comment.user = user.__dict__
        return json.dumps(comments)

def delete_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM comment
        WHERE id = ?
        """, ( id, ))

        rows_affected = db_cursor.rowcount
        success = rows_affected > 0

        # we successfully found and deleted a post with the given id - 
        

        return success
