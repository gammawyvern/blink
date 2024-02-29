from PyQt5.QtWidgets import QMainWindow, QTextEdit, QTabWidget
from PyQt5.QtWidgets import QFileDialog, QPushButton
from PyQt5.QtCore import Qt

class BlinkEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("blink")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        self.tab_widget = QTabWidget(self);
        self.setCentralWidget(self.tab_widget)

        open_button = QPushButton("Open", self)
        open_button.clicked.connect(self.create_tab)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_tab)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(open_button)
        toolbar.addWidget(save_button)

        # self.statusBar()

    def create_tab(self, file_path=None):
        text_buffer = QTextEdit(self) 

        if not file_path:
            file_path, _ = QFileDialog.getOpenFileName(self)

        with open(file_path, 'r') as file:
            content = file.read()
            text_buffer.setPlainText(content)

        self.tab_widget.addTab(text_buffer, "untitled" if not file_path else file_path)

    def save_tab(self):
        current_index = self.tab_widget.currentIndex()
        current_widget = self.tab_widget.widget(current_index)
        file_path, _ = QFileDialog.getSaveFileName(self)

        with open(file_path, 'w') as file:
            content = current_widget.toPlainText()
            file.write(content)

