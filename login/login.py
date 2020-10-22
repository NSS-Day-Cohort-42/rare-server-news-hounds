import sqlite3
import json

def handleLogin(loginCredentials):
  with sqlite3.connect("./rare.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""
    SELECT 
        u.id
    FROM user u
    WHERE u.email = ?    
    """, (loginCredentials['email'], ))    
    data = db_cursor.fetchone()
    
    userMatches = db_cursor.rowcount
    response = {}


    if data != None:
      response['valid'] = True
      response['token'] = data['id']
    else:
      response['valid'] = False

  return json.dumps(response)