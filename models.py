from datetime import datetime
import sqlite3

def init_db():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         content TEXT NOT NULL,
         sender TEXT NOT NULL,
         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

def save_message(content, sender):
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (content, sender) VALUES (?, ?)',
              (content, sender))
    conn.commit()
    conn.close()

def get_chat_history():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('SELECT * FROM messages ORDER BY timestamp')
    messages = c.fetchall()
    conn.close()
    return messages 

def clear_all_messages():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('DELETE FROM messages')
    conn.commit()
    conn.close() 
