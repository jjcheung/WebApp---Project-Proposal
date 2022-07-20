import sqlite3


class Project:
  def __init__(self, title, description, proposer):
    conn = sqlite3.connect("app.db")
    conn.execute("INSERT INTO Project (title, description, proposer) VALUES (%s, %s, %s):", (title, description, proposer))
    conn.close()
    
    