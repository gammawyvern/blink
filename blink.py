from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QPushButton

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("blink")
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        open_button = QPushButton("Open", self)
        open_button.clicked.connect(self.open_file)

        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_file)

        self.statusBar()

        toolbar = self.addToolBar("Toolbar")
        toolbar.addWidget(open_button)
        toolbar.addWidget(save_button)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self)
        with open(file_path, 'r') as file:
            content = file.read()
            self.text_edit.setPlainText(content)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self)
        with open(file_path, 'w') as file:
            content = self.text_edit.toPlainText()
            file.write(content)

if __name__ == "__main__":
    app = QApplication([])

    with open("./style.css", 'r') as file:
        app.setStyleSheet(file.read())

    window = TextEditor()
    window.show()
    app.exec_()

