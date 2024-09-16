import sys
from PyQt5.QtWidgets import QApplication
from GUI.gui import MainWindow  # Upewnij się, że ścieżka importu jest poprawna

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
