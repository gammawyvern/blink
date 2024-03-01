from PyQt5.QtWidgets import QApplication 
from editor import BlinkEditor

import sys
import os

def main():
    app = QApplication([])

    script_dir = os.path.dirname(os.path.abspath(__file__))
    style_file_path = os.path.join(script_dir, "style.css")
    with open(style_file_path, 'r') as file:
        app.setStyleSheet(file.read())

    window = BlinkEditor()
    for file_path in sys.argv[1:]:
        window.load_tab(file_path)

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
