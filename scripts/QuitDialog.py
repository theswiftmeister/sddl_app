from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from guipy.quit_dialog import quit_dialog


class QuitDialog(QDialog, quit_dialog):
    def __init__(self, mainwindow) -> None:
        super().__init__(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.btn_yes.clicked.connect(
            lambda: mainwindow.set_is_save_prompt(True))
        self.btn_yes.clicked.connect(mainwindow.close)
        self.btn_yes.clicked.connect(self.close)
        self.btn_no.clicked.connect(self.close)
        self.btn_save.clicked.connect(mainwindow.save_project)
        self.btn_save.clicked.connect(mainwindow.close)
        self.btn_save.clicked.connect(self.close)
