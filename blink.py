from PyQt5.QtWidgets import QApplication 
from editor import BlinkEditor

import sys;

if __name__ == "__main__":
    app = QApplication([])
    with open("./style.css", 'r') as file:
        app.setStyleSheet(file.read())

    window = BlinkEditor()
    for file_path in sys.argv[1:]:
        window.create_tab(file_path);

    window.show()
    app.exec_()

