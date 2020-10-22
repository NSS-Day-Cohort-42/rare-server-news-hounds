import sqlite3
import json
from models import Post

def get_posts_by_user_id(user_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            p.title,
            p.content,
            p.publication_time,
            p.creation_time,
            p.image,
            p.publish_status,
            p.approve_status,
            p.user_id,
            p.category_id
        FROM post p
        WHERE p.user_id = ?
        """, ( user_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['title'], row['content'], row['publication_time'],
                        row['creation_time'], row['image'], row['publish_status'],
                        row['approve_status'], row['user_id'], row['category_id'])

            posts.append(post.__dict__)

        return json.dumps(posts)