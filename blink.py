from PyQt5.QtWidgets import QApplication 
from editor import BlinkEditor

import sys;

if __name__ == "__main__":
    app = QApplication([])
    with open("./style.css", 'r') as file:
        app.setStyleSheet(file.read())

    window = BlinkEditor()
    if len(sys.argv) > 1:
        for file_path in sys.argv[1:]:
            window.load_tab(file_path);
    else:
        window.create_tab();

    window.show()
    app.exec_()

