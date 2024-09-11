import sqlite3

#connect to db
conn = sqlite3.connect('expense_tracker.db')
c = conn.cursor()

#create schema
c.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
''')

conn.commit()
conn.close()