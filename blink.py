from PyQt5.QtWidgets import QApplication 
from editor import BlinkEditor

import sys;

if __name__ == "__main__":
    file_path = None;
    # TODO ignore other file paths for now
    if len(sys.argv) > 1:
        file_path = sys.argv[1];

    app = QApplication([])

    with open("./style.css", 'r') as file:
        app.setStyleSheet(file.read())

    window = BlinkEditor(file_path)
    window.show()
    app.exec_()

