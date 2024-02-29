from PyQt5.QtWidgets import QMainWindow, QTabWidget, QTextEdit 
from PyQt5.QtWidgets import QFileDialog, QPushButton, QShortcut
from PyQt5.QtCore import Qt, QFileInfo
from PyQt5.QtGui import QKeySequence

class BlinkEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup window information
        self.setWindowTitle("blink")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        # Add widgets to window
        self.tab_widget = QTabWidget(self);
        self.setCentralWidget(self.tab_widget)

        new_button = QPushButton("New", self)
        new_button.clicked.connect(self.create_tab)

        open_button = QPushButton("Open", self)
        open_button.clicked.connect(self.load_tab)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_tab)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(open_button)
        toolbar.addWidget(save_button)

        # Setup keyboard shortcuts
        save_shortcut = QShortcut(QKeySequence.Save, self)
        save_shortcut.activated.connect(self.save_tab)

    def create_tab(self):
        text_buffer = QTextEdit(self) 
        text_buffer.file_path = None;
        file_name = "untitled"

        index = self.tab_widget.addTab(text_buffer, file_name)
        self.tab_widget.setTabPosition(QTabWidget.South)
        self.tab_widget.setCurrentIndex(index)

    def load_tab(self, file_path=None):
        text_buffer = QTextEdit(self) 
        text_buffer.file_path = None;
        file_name = "untitled"

        if not file_path:
            file_path, _ = QFileDialog.getOpenFileName(self)

        # TODO make all these if checks less ugly
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                text_buffer.setPlainText(content)
            file_name = QFileInfo(file_path).fileName();
            text_buffer.file_path = file_path

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

        with open(file_path, 'w') as file:
            content = current_widget.toPlainText()
            file.write(content)

        current_widget.file_path = file_path

        file_info = QFileInfo(file_path)
        file_name = file_info.fileName()
        self.tab_widget.setTabText(current_index, file_name)

