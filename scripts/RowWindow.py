
from datetime import date
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

        self.btn_reset.clicked.connect(self.reset)
        self.select_item_dropbox.textActivated.connect(
            lambda e: self.set_name_unit_fields(e, mainwindow.get_unit_dict()))

    def closeEvent(self, e) -> None:
        return super().closeEvent(e)

    def reset(self):
        """(function)
        Resets every editable widgets in row window."""
        self.set_input_field_values(["", "", "", "", "0"])
        self.dateEdit.setDate(self.todays_date())

    def set_input_field_values(self, list):
        """(function)
        Sets values for inputs fields in row dialog window.

        Params : 
                list : name,quantity,unit,rate,cost"""
        input_fields = [self.input_item_name, self.input_unit, self.input_item_quantity,
                        self.input_item_rate,  self.total_cost_label]
        for index, fields in enumerate(input_fields):
            fields.setText(list[index])

    def get_input_field_values(self):
        """(function)
        Gets values from inputs fields in row dialog window."""
        input_fields = [self.dateEdit, self.input_item_name, self.input_unit,  self.input_item_quantity,
                        self.input_item_rate, self.total_cost_label]
        return [value.text() for value in input_fields]

    def get_input_field(self):
        """(function)
        Gets values from inputs fields in row dialog window."""
        input_fields = [self.input_item_name, self.input_unit,  self.input_item_quantity,
                        self.input_item_rate]
        return input_fields

    def todays_date(self) -> QtCore.QDate:
        """(method)
        Returns : today's date."""
        day = date.today().day
        month = date.today().month
        year = date.today().year
        return QtCore.QDate(year, month, day)

    def set_combo_box(self, dropbox: QComboBox, index: int, is_enabled: bool):
        """(function)

        Sets combo box index and usability.
        """
        if dropbox.count() > 0:
            dropbox.setCurrentIndex(index)
            dropbox.setEnabled(is_enabled)

    def add_dropbox_items(self, dropbox: QComboBox, items: list):
        """Clears dropbox and adds list to items."""
        if dropbox.count() > 0:
            dropbox.clear()
        dropbox.addItems(items)
        dropbox.setCurrentIndex(-1)

    def calculate(self):
        """(method)
        Gets text from quantity and rate, converts it float and sets total cost text."""
        try:
            quantity = int(0 if not self.input_item_quantity.text()
                           else self.input_item_quantity.text())
            rate = float(0 if not self.input_item_rate.text()
                         else self.input_item_rate.text())

            self.total_cost_label.setText(format(quantity*rate, ".2f"))
        except:
            pass

    def set_name_unit_fields(self, current_key: str, dict: dict):
        """(method)
        Set name and unit input, if present in dict.
        Params:
                current_key : str -> key to search.
                dict: dict -> dictionary to search from.
        """
        try:
            for key, value in dict.items():
                if key == current_key:
                    self.input_item_name.setText(key)
                    self.input_unit.setText(value)
        except:
            pass

    def set_window_icon(self, path):
        """(method)
        Set window ui icon.
        Params:
                path :str -> Path of image.
        """
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
