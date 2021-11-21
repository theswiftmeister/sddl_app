from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QTableWidget, QWidget
from guipy.table_widget import table_widget


class TableWidget(QWidget, table_widget):
    def __init__(self, mainwindow) -> None:
        super().__init__()
        self.setupUi(self)
        self.main = mainwindow

    def set_table(self):
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSortingEnabled(True)

        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

    def get_table_widget(self) -> QTableWidget:
        return self.tableWidget
