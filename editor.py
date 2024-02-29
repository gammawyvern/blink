from PyQt5.QtWidgets import QMainWindow, QTabWidget, QTextEdit 
from PyQt5.QtWidgets import QFileDialog, QPushButton, QShortcut
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QKeySequence

import os

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
        new_button.clicked.connect(self.create_tab)

        open_button = QPushButton("Open", self)
        open_button.clicked.connect(self.load_tab)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_tab)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(new_button)
        toolbar.addWidget(open_button)
        toolbar.addWidget(save_button)

    ########################################
    # Tab control / file io
    ########################################

    def create_tab(self):
        text_buffer = QTextEdit(self) 
        text_buffer.file_path = None;
        file_name = "untitled"

        index = self.tab_widget.addTab(text_buffer, file_name)
        self.tab_widget.setTabPosition(QTabWidget.South)
        self.tab_widget.setCurrentIndex(index)

    def load_tab(self, file_path=None):
        text_buffer = QTextEdit(self) 
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

    def save_tab(self):
        current_index = self.tab_widget.currentIndex()
        current_widget = self.tab_widget.widget(current_index)

        if getattr(current_widget, 'file_path', None):
            file_path = current_widget.file_path
        else:
            file_path, _ = QFileDialog.getSaveFileName(self)

        if file_path:
            with open(file_path, 'w') as file:
                content = current_widget.toPlainText()
                file.write(content)

            current_widget.file_path = file_path

            file_info = QFileInfo(file_path)
            file_name = file_info.fileName()
            self.tab_widget.setTabText(current_index, file_name)

    ########################################
    # Shortcut setup / functions
    ########################################

    def setup_shorcuts(self):
        new_shortcut = QShortcut(Qt.CTRL + Qt.Key_T, self)
        new_shortcut.activated.connect(self.create_tab)

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

    def next_tab(self):
        current_index = (self.tab_widget.currentIndex() + 1) % self.tab_widget.count()
        self.tab_widget.setCurrentIndex(current_index)

    def prev_tab(self):
        current_index = (self.tab_widget.currentIndex() - 1) % self.tab_widget.count()
        self.tab_widget.setCurrentIndex(current_index)

    def delete_current_tab(self):
        current_index = self.tab_widget.currentIndex()
        self.tab_widget.removeTab(current_index)

