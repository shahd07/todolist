import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox,QMainWindow,QListWidget
from PyQt5.uic import loadUi
class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.done = False
class TodoList(QMainWindow):
    def __init__(self):
        super(TodoList,self).__init__()
        loadUi('todo.ui',self)
        self.tasks = []
        # layout and window properties
        self.setWindowTitle('Todo List')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_list = TodoList()
    todo_list.show()
    sys.exit(app.exec_())

