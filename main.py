from PyQt5.QtWidgets import QApplication
from scripts.MainWindow import MainWindow
from scripts.WarningDialog import WarningWindow

# Main executable file.
if __name__ == "__main__":
    import sys
    import os
    app = QApplication(sys.argv)
    if os.getenv("USER_NAME") in ["RKB"]:
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    else:
        window = WarningWindow()
        window.set_window("User does not have permission.", ["ok"])
        window.show()
        sys.exit(app.exec_())

# TO DO
"""


"""
