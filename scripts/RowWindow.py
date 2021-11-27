
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

        self.btn_reset.clicked.connect(lambda: self.set_column_field_texts(
            ["", "", "", "", ""]))

        self.select_tab_dropbox.textActivated.connect(lambda e: self.set_dropbox_current_index(
            self.select_item_dropbox, [k for k, v in mainwindow.get_name_value_dict()[self.get_dropbox_current_index(self.select_tab_dropbox)].items()]))
        self.select_item_dropbox.textActivated.connect(
            lambda e: self.set_name_value_fields(name=e, tab_index=self.get_dropbox_current_index(self.select_tab_dropbox), list=mainwindow.get_name_value_dict()))

    def closeEvent(self, e) -> None:
        return super().closeEvent(e)

    def get_dropbox_current_index(self, dropbox: QComboBox):
        return dropbox.currentIndex()

    def set_dropbox_current_index(self, dropbox: QComboBox, list: list):
        dropbox.clear()
        dropbox.addItems(list)

    def calculate(self):
        try:
            quantity = int(0 if not self.input_item_quantity.text()
                           else self.input_item_quantity.text())
            rate = float(0 if not self.input_item_rate.text()
                         else self.input_item_rate.text())

            self.total_cost_label.setText(format(quantity*rate, ".2f"))
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

    def get_column_field_texts(self):
        columns = [self.input_item_name, self.input_unit,
                   self.input_item_quantity, self.input_item_rate]
        return columns

    def set_name_value_fields(self, name, tab_index, list):
        self.input_item_name.setText(name)
        self.input_unit.setText(
            list[tab_index][name])

    def get_name_value_dict(self):
        name = self.input_item_name.text()
        value = self.input_unit.text()
        return name, value

    def set_dropbox(self, dropbox: QComboBox, isEnabled: bool, index: int):
        dropbox.setCurrentIndex(index)
        dropbox.setEnabled(isEnabled)

    def set_window_icon(self, path):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
