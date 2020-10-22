import sqlite3
import json

def handleLogin(loginCredentials):
  with sqlite3.connect("./rare.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()
    db_cursor.execute("""
    SELECT 
        u.id,
        u.password
    FROM user u
    WHERE u.email = ?    
    """, (loginCredentials['email'], ))    
    data = db_cursor.fetchone()
    
    userMatches = db_cursor.rowcount
    response = {}

    try:
      if data['password'] == loginCredentials['password']:
        response['valid'] = True
        response['token'] = data['id']
    except TypeError:
      response['valid'] = False
      pass

  return json.dumps(response)