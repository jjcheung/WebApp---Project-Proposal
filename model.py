import sqlite3
class Project:
  def __init__(self, title, description, proposer):
    conn = sqlite3.connect("app.db")
    sql = "INSERT INTO Project (title, description, proposer) VALUES (?, ?, ?);"
    values = (title, description, proposer)
    conn.execute(sql, values)
    conn.commit()
    conn.close()
  
      
  def select_all():
    conn = sqlite3.connect("app.db")
    sql = "SELECT id, title, description, proposer FROM Project;"
    cursor = conn.execute(sql)
    data = []
    for record in cursor:
        data.append(record)
    conn.close()
    return data
  
  def delete(pid):
    conn = sqlite3.connect("app.db")
    sql = "DELETE FROM Project WHERE ID = ?;"
    values = (int(pid), )
    conn.execute(sql, values)
    conn.commit()
    conn.close()
