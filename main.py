from PyQt6.QtWidgets import QApplication
import sys
from logic import LogicWindow

def main():
    app = QApplication(sys.argv)
    window = LogicWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
