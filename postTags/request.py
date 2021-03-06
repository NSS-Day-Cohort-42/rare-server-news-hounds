import sqlite3
import json
from models import PostTag, Tag

def get_postTag_by_post_id(postId):
	with sqlite3.connect("./rare.db") as conn:
		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()
		db_cursor.execute("""
		SELECT
		pt.id,
		pt.post_id,
		pt.tag_id,
		t.name
		FROM post_tag pt
		JOIN tag t on t.id = pt.tag_id
		WHERE pt.post_id = ?
		""", ( postId, ))

		postTags = []
		dataset = db_cursor.fetchall()

		for row in dataset:
			postTag = PostTag(row['id'], row['post_id'], row['tag_id'])
			postTags.append(postTag.__dict__)
			tag = Tag(row['tag_id'], row['name'])
			postTag.tag = tag.__dict__

	return json.dumps(postTags)

def create_postTag(new_postTag):
	with sqlite3.connect("./rare.db") as conn:
		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()
		db_cursor.execute("""
		INSERT INTO post_tag
			( post_id, tag_id )
		VALUES
			(?, ?);
		""", (new_postTag['post_id'], new_postTag['tag_id']) )
		id = db_cursor.lastrowid
		new_postTag['id'] = id
	return json.dumps(new_postTag)

def delete_postTag(postTagId):
	with sqlite3.connect("./rare.db") as conn:
		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()
		db_cursor.execute("""
		DELETE FROM post_tag
		WHERE id = ?
		""", (postTagId, ) )

		rows_affected = db_cursor.rowcount

		if rows_affected == 0:
			return False
		else:
			return True