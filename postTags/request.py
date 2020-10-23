import sqlite3
import json
from models import PostTag

def get_post_tag_by_post_id(postId):
  with sqlite3.connect("./rare.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""
    SELECT
        pt.id,
        pt.post_id,
        pt.tag_id
    FROM post_tag pt
    WHERE pt.post_id = ?
    """, ( postId, ))

    postTags = []
    dataset = db_cursor.fetchall()

    for row in dataset:
        postTag = PostTag(row['id'], row['post_id'], row['tag_id'])

        postTags.append(postTag.__dict__)

  return json.dumps(postTags)