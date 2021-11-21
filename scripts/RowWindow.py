
from PyQt5 import QtCore
from PyQt5.QtWidgets import QComboBox, QDialog
from guipy.add_row_dialog import add_row_dialog


class RowWindow(QDialog, add_row_dialog):
    def __init__(self, mainwindow) -> None:
        super().__init__(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.input_item_quantity.editingFinished.connect(self.calculate)
        self.input_item_rate.editingFinished.connect(self.calculate)

        self.btn_ok.clicked.connect(lambda: mainwindow.add_to_table(
            self.select_tab_dropbox.currentIndex(), self.column_texts()))

    def closeEvent(self, e) -> None:
        return super().closeEvent(e)

    def add_dropbox_items(self, dropbox: QComboBox, item: str):
        dropbox.addItem(item)
        dropbox.setCurrentIndex(-1)

    def remove_dropbox_item(self, dropbox: QComboBox, index: int):
        dropbox.removeItem(index)

    def clear_dropbox_items(self):
        self.select_tab_dropbox.clear()
        self.select_item_dropbox.clear()

    def calculate(self):
        try:
            quantity = int(0 if not self.input_item_quantity.text()
                           else self.input_item_quantity.text())
            rate = float(0 if not self.input_item_rate.text()
                         else self.input_item_rate.text())
            self.total_cost_label.setText(str(quantity*rate))
        except:
            pass

    def column_texts(self):
        columns = [self.dateEdit, self.input_item_name, self.input_unit,
                   self.input_item_quantity, self.input_item_rate, self.total_cost_label]
        return [i.text() for i in columns]

    def column_fields(self):
        columns = [self.input_item_name, self.input_unit,
                   self.input_item_quantity, self.input_item_rate, self.total_cost_label]
        return columns

    def get_name_value_dict(self):
        name = self.input_item_name.text()
        value = self.input_unit.text()
        return name, value

    def set_dropbox(self, dropbox: QComboBox, visibility: bool, index: int):
        dropbox.setCurrentIndex(index)
        dropbox.setEnabled(visibility)
