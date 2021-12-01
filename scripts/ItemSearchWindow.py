from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from guipy.item_search_dialog import item_search_dialog


class ItemSearchWindow(QDialog, item_search_dialog):
    def __init__(self, mainwindow) -> None:
        super().__init__(None, QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.btn_print.clicked.connect(
            lambda: mainwindow.print_preview_widget(self.tableWidget, f"{mainwindow.windowTitle()}-{self.windowTitle()}", self.label_total_cost.text()))

    def closeEvent(self, e) -> None:
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        return super().closeEvent(e)

    def set_table(self, window_title, current_table):
        self.tableWidget.setColumnCount(4)
        for index, name in enumerate(["Date", "Quantity", "Rate", "Total Cost"]):
            self.tableWidget.setHorizontalHeaderItem(
                index, QTableWidgetItem(name))
            self.tableWidget.horizontalHeader().setSectionResizeMode(index, QHeaderView.Stretch)

        self.setWindowTitle(window_title.title())
        matched_rows = []
        for i in range(current_table.rowCount()):
            is_match = current_table.item(
                i, 1).text().lower() == window_title.lower()
            if is_match:
                matched_rows.append(i)

        self.tableWidget.setRowCount(len(matched_rows))
        for col_id, col in enumerate([0, 3, 4, 5]):
            for row_id, row in enumerate(matched_rows):
                item = QTableWidgetItem(current_table.item(row, col).text())
                self.tableWidget.setItem(row_id, col_id, item)
                self.tableWidget.item(row_id, col_id).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignCenter)

        self.get_table_total_cost(3)
        self.resize(400, 600)

    def set_whole_project(self, window_title, current_table_items):
        self.setWindowTitle(window_title.title())
        self.tableWidget.setColumnCount(6)
        for index, name in enumerate(["Date", "Name", "Unit", "Quantity", "Rate", "Total Cost"]):
            self.tableWidget.setHorizontalHeaderItem(
                index, QTableWidgetItem(name))
            self.tableWidget.horizontalHeader().setSectionResizeMode(index, QHeaderView.Stretch)

        self.tableWidget.setRowCount(len(current_table_items))
        for row in range(len(current_table_items)):
            for col in range(self.tableWidget.columnCount()):
                item = QTableWidgetItem(current_table_items[row][col])
                self.tableWidget.setItem(row, col, item)
                self.tableWidget.item(row, col).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignCenter)

        self.get_table_total_cost(5)
        self.resize(600, 600)

    def get_table_total_cost(self, total_cost_index):
        table = self.tableWidget
        total_table_cost = format(sum([float(table.item(i, total_cost_index).text()) for i in range(table
                                                                                                    .rowCount())]), ".2f")
        self.label_total_cost.setText(total_table_cost)

    def set_table_font(self, font_family, font_size):
        font = self.tableWidget.font()
        font.setFamily(font_family)
        font.setPointSize(int(font_size))
        self.tableWidget.setFont(font)
        self.label.setFont(font)
        self.label_total_cost.setFont(font)
