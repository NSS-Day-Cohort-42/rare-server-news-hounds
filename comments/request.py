import sqlite3
import json


def delete_post(id):
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