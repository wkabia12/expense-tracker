from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('expense_tracker.db')

#Landing Page

@app.route('/')
def index():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM expenses ORDER BY date DESC')
    expenses = c.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

# Add Expenses Route
@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        description = request.form['description']
        category = request.form['category']
        amount = request.form['amount']
        date = datetime.now().strftime('%Y-%m-%d')

        conn = connect_db()
        c = conn.cursor()
        c.execute("INSERT INTO expenses (description, category, amount, date) VALUES(?, ?, ?, ?)", (description, category, amount, date))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    return render_template('add_expenses.html')

if __name__ == '__main__':
    app.run(debug=True)