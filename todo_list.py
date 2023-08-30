import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QComboBox
from PyQt5.uic import loadUi

class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.done = False

class TodoList(QWidget):
    def __init__(self):
        super(TodoList,self).__init__()
        loadUi('todo.ui',self)
        self.tasks = []
        self.initUI()

    def initUI(self):
        self.task_name_label = QLabel('Task Name')
        self.task_name_input = QLineEdit()
        self.due_date_label = QLabel('Due Date')
        self.due_date_input = QLineEdit()
        self.add_button = QPushButton('Add Task')
        self.sort_by_label = QLabel('Sort By')
        self.sort_by_combo_box = QComboBox()
        self.sort_by_combo_box.addItem('Alphabetical')
        self.sort_by_combo_box.addItem('Due Date')
        self.search_label = QLabel('Search')
        self.search_input = QLineEdit()
        self.delete_button = QPushButton('Delete Task')

        # layout
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.task_name_label)
        hbox1.addWidget(self.task_name_input)
        hbox1.addWidget(self.due_date_label)
        hbox1.addWidget(self.due_date_input)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.add_button)
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.sort_by_label)
        hbox2.addWidget(self.sort_by_combo_box)
        hbox2.addWidget(self.search_label)
        hbox2.addWidget(self.search_input)
        
        vbox.addLayout(hbox2)
        
        vbox.addWidget(self.delete_button)

        # Connect signals to slots
        self.add_button.clicked.connect(self.add_task)
        
        self.delete_button.clicked.connect(self.delete_task)

        # layout and window properties
        self.setLayout(vbox)
        self.setWindowTitle('Todo List')

    def add_task(self):
        
            name = self.task_name_input.text()
            due_date = self.due_date_input.text()

            task = Task(name, due_date)

            self.tasks.append(task)

    def delete_task(self):
        
            name_to_delete=self.task_name_input.text()
            
            for task in self.tasks:
                if task.name==name_to_delete:
                    self.tasks.remove(task)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_list = TodoList()
    todo_list.show()
    sys.exit(app.exec_())
