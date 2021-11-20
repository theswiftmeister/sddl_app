from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from guipy.main_window import MainWindow
from scripts.TabWindow import TabWindow
from scripts.RowWindow import RowWindow
from scripts.TableWidget import TableWidget


class MainWindow(QMainWindow, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.table_list = []

        self.tab_window = TabWindow(self)
        self.row_window = RowWindow(self)

        # Button events
        self.btn_add_tab.clicked.connect(self.open_tab_window)
        self.btn_remove_tab.clicked.connect(self.remove_tab)
        self.btn_add_row.clicked.connect(self.open_row_window)

        self.add_tab("Project")

    def open_tab_window(self):
        self.tab_window.show()

    def open_row_window(self):
        self.row_window.show()

    def add_tab(self, tab_name):
        table = TableWidget()
        table.set_table()
        self.tabWidget.addTab(table, tab_name)
        if self.tabWidget.count() > 1:
            self.table_list.append(table)
            self.row_window.add_dropbox_items(
                self.row_window.select_tab_dropbox, tab_name)

    def remove_tab(self):
        if self.tabWidget.currentIndex() != 0:
            self.tabWidget.removeTab(self.tabWidget.currentIndex())

    def add_row(self, index, list):
        table = self.table_list[index].get_table_widget()
        row = table.rowCount()
        table.setRowCount(row+1)
        for i in range(table.columnCount()):
            item = QTableWidgetItem(list[i])
            table.setItem(row, i, item)
            table.item(row, i).setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignCenter)
