from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from guipy.item_search_dialog import item_search_dialog


class ItemSearchWindow(QDialog, item_search_dialog):
    def __init__(self, mainwindow) -> None:
        super().__init__(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

    def closeEvent(self, e) -> None:
        self.tableWidget.setRowCount(0)
        return super().closeEvent(e)

    def set_table(self, window_title, current_table):
        self.setWindowTitle(window_title.title())
        matched_rows = []
        for i in range(current_table.rowCount()):
            is_match = current_table.item(
                i, 1).text().lower() == window_title.lower()
            if is_match:
                matched_rows.append(i)

        self.tableWidget.setRowCount(len(matched_rows))
        for col_id, col in enumerate([0, 3, 4, 5, ]):
            for row_id, row in enumerate(matched_rows):
                item = QTableWidgetItem(current_table.item(row, col).text())
                self.tableWidget.setItem(row_id, col_id, item)
                self.tableWidget.item(row_id, col_id).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignCenter)

        self.get_table_total_cost()

    def get_table_total_cost(self):
        table = self.tableWidget
        column = 3
        total_table_cost = sum([float(table.item(i, column).text()) for i in range(table
                                                                                   .rowCount())])
        self.label_total_cost.setText(str(total_table_cost))

    def set_table_font(self, font_family, font_size):
        font = self.tableWidget.font()
        font.setFamily(font_family)
        font.setPointSize(int(font_size))
        self.tableWidget.setFont(font)
        self.label.setFont(font)
        self.label_total_cost.setFont(font)
