
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QComboBox, QDialog
from guipy.add_row_dialog import add_row_dialog


class RowWindow(QDialog, add_row_dialog):
    def __init__(self, mainwindow) -> None:
        super().__init__(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.input_item_quantity.editingFinished.connect(self.calculate)
        self.input_item_rate.editingFinished.connect(self.calculate)

    def closeEvent(self, e) -> None:
        return super().closeEvent(e)

    def add_dropbox_items(self, dropbox: QComboBox, item: str):
        dropbox.addItem(item)
        dropbox.setCurrentIndex(-1)

    def remove_dropbox_item(self, dropbox: QComboBox, index: int):
        dropbox.removeItem(index-1)

    def get_dropbox_current_index(self, dropbox: QComboBox):
        return dropbox.currentIndex()

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
        return [i.text() for i in columns][:]

    def set_column_field_texts(self, list):
        columns = [self.input_item_name, self.input_unit,
                   self.input_item_quantity, self.input_item_rate, self.total_cost_label]
        for i in range(len(columns)):
            columns[i].setText(list[i])

    def get_name_value_dict(self):
        name = self.input_item_name.text()
        value = self.input_unit.text()
        return name, value

    def set_dropbox(self, dropbox: QComboBox, visibility: bool, index: int):
        dropbox.setCurrentIndex(index)
        dropbox.setEnabled(visibility)

    def set_window_icon(self, path):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
