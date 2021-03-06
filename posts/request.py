from models.user import User
import sqlite3
import json
from models import Post, Category

def get_all_posts():
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
            p.category_id,
            c.name category_name,
            u.username,
            u.first_name,
            u.last_name
        FROM post p
        JOIN Category c on c.id = p.category_id
        JOIN user u on u.id = p.user_id
        """)
        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['content'], row['publication_time'],
                        row['creation_time'], row['image'], row['publish_status'],
                        row['approve_status'], row['user_id'], row['category_id'])
            category = Category(row['category_id'], row['category_name'])
            user = User(row['user_id'], row['first_name'], row['last_name'], row['username'], "", "")
            post.category = category.__dict__
            post.user = user.__dict__
            posts.append(post.__dict__)

        return json.dumps(posts)

def get_single_post(id):
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
            p.category_id,
            c.name category_name,
            u.username,
            u.first_name,
            u.last_name
        FROM post p
        JOIN Category c on c.id = p.category_id
        JOIN user u on u.id = p.user_id
        WHERE p.id = ?    
        """, (id, ))    
        row = db_cursor.fetchone()
        if row:
            post = Post(row['id'], row['title'], row['content'], row['publication_time'],
                    row['creation_time'], row['image'], row['publish_status'],
                    row['approve_status'], row['user_id'], row['category_id'])
            category = Category(row['category_id'], row['category_name'])
            user = User(row['user_id'], row['first_name'], row['last_name'], row['username'], "", "")
            post.category = category.__dict__
            post.user = user.__dict__
            return json.dumps(post.__dict__)
        else:
            return False



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
            p.category_id,
            c.name category_name,
            u.username,
            u.first_name,
            u.last_name
        FROM post p
        JOIN Category c on c.id = p.category_id
        JOIN user u on u.id = p.user_id
        WHERE p.user_id = ?
        """, ( user_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['content'], row['publication_time'],
                        row['creation_time'], row['image'], row['publish_status'],
                        row['approve_status'], row['user_id'], row['category_id'])

            posts.append(post.__dict__)

            category = Category(row['category_id'], row['category_name'])
            user = User(row['user_id'], row['first_name'], row['last_name'], row['username'], "", "")
            post.category = category.__dict__
            post.user = user.__dict__

        return json.dumps(posts)

def get_posts_by_category_id(category_id):
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
            p.category_id,
            c.name category_name,
            u.username,
            u.first_name,
            u.last_name
        FROM post p
        JOIN Category c on c.id = p.category_id
        JOIN user u on u.id = p.user_id
        WHERE p.category_id = ?
        """, ( category_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['content'], row['publication_time'],
                        row['creation_time'], row['image'], row['publish_status'],
                        row['approve_status'], row['user_id'], row['category_id'])

            posts.append(post.__dict__)
            user = User(row['user_id'], row['first_name'], row['last_name'], row['username'], "", "")
            category = Category(row['category_id'], row['category_name'])
            post.category = category.__dict__
            post.user = user.__dict__


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

            db_cursor.execute("""
            DELETE FROM comment
            WHERE post_id = ?
            """, ( id, ))

        return success

def update_post(id, post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE post 
        SET
            title = ?,
            content = ?,
            publication_time = ?,
            image = ?,
            publish_status = ?,
            approve_status = ?,
            user_id = ?,
            category_id = ?
        WHERE id = ?
        """, (post['title'], post['content'], post['publication_time'], post['image'], post['publish_status'], post['approve_status'], post['user_id'], post['category_id'], id, ) )
        if db_cursor.rowcount == 0:
            return False
        else: 
            return True
