from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from guipy.warning_dialog import warning_dialog


class WarningWindow(QDialog, warning_dialog):
    def __init__(self) -> None:
        super().__init__(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

    def closeEvent(self, a0) -> None:
        self.warning_text_label.setText("")
        self.buttonBox.clear()

        return super().closeEvent(a0)

    def set_window(self, str, btns):
        self.warning_text_label.setText(str)
        font = self.warning_text_label.font()
        self.warning_text_label.setFont(font)
        for i in range(len(btns)):
            if btns[i] == 'ok':
                self.buttonBox.addButton(
                    "OK", QDialogButtonBox.ButtonRole.AcceptRole)
            if btns[i] == 'yes':
                self.buttonBox.addButton(
                    "YES", QDialogButtonBox.ButtonRole.AcceptRole)
            if btns[i] == 'no':
                self.buttonBox.addButton(
                    "NO", QDialogButtonBox.ButtonRole.RejectRole)
