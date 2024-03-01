from PyQt5.QtWidgets import QMainWindow, QTabWidget, QTextEdit 
from PyQt5.QtWidgets import QFileDialog, QPushButton, QShortcut
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QKeySequence

import os

########################################
# Decorator to update focus
########################################

from functools import wraps

def update_focus_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.update_focus()
        return result
    return wrapper

########################################
# Main blink text editor class
########################################

class BlinkEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("blink")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        self.setup_layout()
        self.setup_shorcuts()

    def setup_layout(self):
        self.tab_widget = QTabWidget(self);
        self.setCentralWidget(self.tab_widget)

        new_button = QPushButton("New", self)
        new_button.clicked.connect(lambda event: self.create_tab())

        open_button = QPushButton("Open", self)
        open_button.clicked.connect(lambda event: self.load_tab())

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(lambda event: self.save_tab())

        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(new_button)
        toolbar.addWidget(open_button)
        toolbar.addWidget(save_button)

    ########################################
    # Decorator functions 
    ########################################

    def update_focus(self):
        current_index = self.tab_widget.currentIndex()

        if current_index != -1:
            current_widget = self.tab_widget.widget(current_index)
            current_widget.setFocus()

    ########################################
    # Tab control / file io
    ########################################

    @update_focus_decorator
    def create_tab(self):
        text_buffer = QTextEdit(self) 
        text_buffer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        text_buffer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        text_buffer.file_path = None;
        file_name = "untitled"

        index = self.tab_widget.addTab(text_buffer, file_name)
        self.tab_widget.setTabPosition(QTabWidget.South)
        self.tab_widget.setCurrentIndex(index)
        text_buffer.setFocus()

    @update_focus_decorator
    def load_tab(self, file_path=None):
        text_buffer = QTextEdit(self) 
        text_buffer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        text_buffer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        file_name = "untitled"

        if not file_path:
            file_path, _ = QFileDialog.getOpenFileName(self)

        if file_path:
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    content = file.read()
                    text_buffer.setPlainText(content)

            text_buffer.file_path = file_path;
            file_name = QFileInfo(file_path).fileName();

            index = self.tab_widget.addTab(text_buffer, file_name)
            self.tab_widget.setTabPosition(QTabWidget.South)
            self.tab_widget.setCurrentIndex(index)
            text_buffer.setFocus()

    @update_focus_decorator
    def save_tab(self):
        current_index = self.tab_widget.currentIndex()
        current_widget = self.tab_widget.widget(current_index)

        if current_index == -1:
            return

        file_path = getattr(current_widget, 'file_path', None)
        if not file_path:
            file_path, _ = QFileDialog.getSaveFileName(self)

        if file_path:
            with open(file_path, 'w') as file:
                content = current_widget.toPlainText()
                file.write(content)

            current_widget.file_path = file_path
            file_name = QFileInfo(file_path).fileName()

            self.tab_widget.setTabText(current_index, file_name)

    ########################################
    # Shortcut setup / functions
    ########################################

    def setup_shorcuts(self):
        new_shortcut_n = QShortcut(Qt.CTRL + Qt.Key_N, self)
        new_shortcut_t = QShortcut(Qt.CTRL + Qt.Key_T, self)
        new_shortcut_n.activated.connect(self.create_tab)
        new_shortcut_t.activated.connect(self.create_tab)

        open_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_O), self)
        open_shortcut.activated.connect(self.load_tab)

        save_shortcut = QShortcut(Qt.CTRL + Qt.Key_S, self)
        save_shortcut.activated.connect(self.save_tab)

        next_tab_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Tab), self)
        next_tab_shortcut.activated.connect(self.next_tab)

        prev_tab_shortcut = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_Tab), self)
        prev_tab_shortcut.activated.connect(self.prev_tab)

        del_tab_shortcut = QShortcut(Qt.CTRL + Qt.Key_W, self)
        del_tab_shortcut.activated.connect(self.delete_current_tab)

    @update_focus_decorator
    def next_tab(self):
        current_index = (self.tab_widget.currentIndex() + 1) % self.tab_widget.count()
        self.tab_widget.setCurrentIndex(current_index)

    @update_focus_decorator
    def prev_tab(self):
        current_index = (self.tab_widget.currentIndex() - 1) % self.tab_widget.count()
        self.tab_widget.setCurrentIndex(current_index)

    @update_focus_decorator
    def delete_current_tab(self):
        current_index = self.tab_widget.currentIndex()
        self.tab_widget.removeTab(current_index)

    ########################################
    # Syntax highlighting
    ########################################

