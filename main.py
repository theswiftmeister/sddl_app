from PyQt5.QtWidgets import QApplication
from scripts.MainWindow import MainWindow


# Main executable file.

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# TO DO
"""

"""
