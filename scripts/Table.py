from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView, QTableWidgetItem
from scripts.Cell import Cell

from scripts.Row import Row


class Table(object):
    def __init__(self) -> None:
        """(class)
        Table object. Creates a table wigdet.Has fixed columns.\n
        """
        super().__init__()
        self.column_names = ["Date", "Name",
                             "Unit", "Quantity",  "Rate", "Total Amount"]

        self.table = QTableWidget()
        self.rows = []

    def create_table(self):
        """(method)
        Returns : self.table
        """
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSortingEnabled(True)
        self.table.setColumnCount(len(self.column_names))
        self.table.setRowCount(0)

        for index, name in enumerate(self.column_names):
            self.table.setHorizontalHeaderItem(index, QTableWidgetItem(name))
            self.table.horizontalHeader().setSectionResizeMode(index, QHeaderView.Stretch)

        return self.table

    def add_row(self, row_item: Row):
        """(method)
        Add rows to table.
        Params:
                row_item : Row object
                row_data : list of text for cells
        """
        # Add row to table.
        self.rows.append(row_item)

        # Increase table row count.
        row = self.table.rowCount()
        self.table.setRowCount(row+1)

        for index, cell in enumerate(row_item.get_item()):
            self.set_table_item(row, cell)

    def edit_row(self, current_row: int, row_data: list):
        row_item: Row = self.rows[current_row]
        row_item.set_item(row_data)
        for index, cell in enumerate(row_item.get_item()):
            self.set_table_item(current_row, cell)

    def insert_row(self, row: int, row_data: Row):
        self.rows.insert(row, row_data)
        self.table.insertRow(row)
        for index, cell in enumerate(row_data.get_item()):
            self.set_table_item(row, cell)

    def delete_row(self, current_row: int):
        self.rows.pop(current_row)
        self.table.removeRow(current_row)

    def set_table_item(self, row: int, cell: Cell):
        item = QTableWidgetItem(cell.get_text())
        self.table.setItem(row, cell.get_column(), item)
        self.table.item(row, cell.get_column()).setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        return item

    def current_row(self):
        return self.table.currentRow()

    def get_rows(self):
        """(method)
        Returns : Table row object list"""
        return self.rows

    def get_table(self):
        return self.table
