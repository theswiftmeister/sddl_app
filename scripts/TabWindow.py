from PyQt5.QtWidgets import QDialog
from guipy.add_tab_dialog import add_tab_dialog


class TabWindow(QDialog, add_tab_dialog):
    def __init__(self, mainwindow) -> None:
        super().__init__()
        self.setupUi(self)
        self.button_ok.clicked.connect(
            lambda: mainwindow.add_tab(self.get_tab_name_text()))
        self.button_ok.clicked.connect(self.close)

    def get_tab_name_text(self) -> str:
        return self.input_tab_name.text()
