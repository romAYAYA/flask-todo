import sqlite3
from flask import Flask, render_template, request, redirect, url_for

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    task TEXT
)
''')
conn.commit()
conn.close()

app = Flask(__name__)


@app.route('/')
def tasks_page():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, task FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('tasks.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
        conn.commit()
        conn.close()

    return redirect(url_for('tasks_page'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
