import sys
import sqlite3
from PyQt6.QtWidgets import QTextBrowser, QApplication, QMainWindow


class TodoDesktop(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task List")
        self.setGeometry(100, 100, 400, 300)

        self.text_browser = QTextBrowser(self)
        self.text_browser.setGeometry(10, 10, 380, 280)

        self.show_tasks()

    def show_tasks(self):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, task FROM tasks')
        tasks = cursor.fetchall()
        conn.close()

        task_list = [f'{task[0]}. {task[1]}' for task in tasks]
        self.text_browser.setPlainText('\n'.join(task_list))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TodoDesktop()
    window.show()
    sys.exit(app.exec())
