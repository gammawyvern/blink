from PyQt5.QtWidgets import QMainWindow, QTextEdit, QFileDialog, QPushButton
from PyQt5.QtCore import Qt

class BlinkEditor(QMainWindow):
    def __init__(self, file_path=None):
        super().__init__()

        self.setWindowTitle("blink")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        open_button = QPushButton("Open", self)
        open_button.clicked.connect(self.open_file)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_file)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(open_button)
        toolbar.addWidget(save_button)

        # self.statusBar()

        if file_path:
            self.open_file(file_path);

    def open_file(self, file_path=None):
        if not file_path:
            file_path, _ = QFileDialog.getOpenFileName(self)

        with open(file_path, 'r') as file:
            content = file.read()
            self.text_edit.setPlainText(content)

    def save_file(self, file_path=None):
        if not file_path:
            file_path, _ = QFileDialog.getSaveFileName(self)

        with open(file_path, 'w') as file:
            content = self.text_edit.toPlainText()
            file.write(content)

