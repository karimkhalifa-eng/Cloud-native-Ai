import sqlite3

conn = sqlite3.connect('agent.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS agent_request (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT, tool TEXT, result TEXT)''')

conn.commit()

def save_request(message, tool, result):
    cursor.execute('INSERT INTO agent_request (message, tool, result) VALUES (?, ?, ?)', (message, tool, result))
    conn.commit()