import sqlite3
import json
from models import Post

def get_posts_by_user_id(user_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            p.id,
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
            post = Post(row['id'], row['title'], row['content'], row['publication_time'],
                        row['creation_time'], row['image'], row['publish_status'],
                        row['approve_status'], row['user_id'], row['category_id'])

            posts.append(post.__dict__)

        return json.dumps(posts)

def create_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO post
            ( title, content, publication_time, creation_time, image, publish_status, approve_status, user_id, category_id )
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (new_post['title'], new_post['content'], new_post['publication_time'], new_post['creation_time'], new_post['image'], new_post['publish_status'], new_post['approve_status'], new_post['user_id'], new_post['category_id']))
    id = db_cursor.lastrowid
    new_post['id'] = id
    return json.dumps(new_post)

def delete_post(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM post
        WHERE id = ?
        """, ( id, ))

        rows_affected = db_cursor.rowcount
        success = rows_affected > 0

        # we successfully found and deleted a post with the given id - 
        # now delete any post_tag rows with this post_id
        if(success):
            db_cursor.execute("""
            DELETE FROM post_tag
            WHERE post_id = ?
            """, ( id, ))

        return success