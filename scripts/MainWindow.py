from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from guipy.main_window import MainWindow
from scripts.TabWindow import TabWindow
from scripts.RowWindow import RowWindow
from scripts.ItemSearchWindow import ItemSearchWindow
from scripts.TableWidget import TableWidget


class MainWindow(QMainWindow, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.table_list = []
        self.tab_items_list = []

        self.tab_window = TabWindow(self)
        self.row_window = RowWindow(self)
        self.item_search_window = ItemSearchWindow(self)

        # Button events
        self.btn_add_tab.clicked.connect(self.open_tab_window)
        self.btn_remove_tab.clicked.connect(self.remove_tab)
        self.btn_add_row.clicked.connect(self.open_row_window)
        self.btn_remove_row.clicked.connect(self.remove_row_item)
        self.btn_search_item.clicked.connect(self.open_item_search_window)

        self.tabWidget.currentChanged.connect(lambda e: self.on_tab_changed(e))
        self.fontComboBox.textActivated.connect(
            lambda w: self.change_table_styleSheet(w))
        self.spinBox.textChanged.connect(
            lambda e: self.change_table_fontSize(e))
        self.add_tab("Project")

    def open_tab_window(self):
        self.tab_window.show()

    def open_row_window(self):
        for i in self.row_window.column_fields():
            i.setText("")
        is_first_tab = True if self.tabWidget.currentIndex() == 0 else False
        self.row_window.set_dropbox(
            self.row_window.select_tab_dropbox, is_first_tab, self.tabWidget.currentIndex()-1)
        self.row_window.show()

    def open_item_search_window(self):
        self.item_search_window.set_table(
            self.dropdown.currentText(), self.table_list[self.tabWidget.currentIndex()].get_table_widget())
        self.item_search_window.set_table_font(
            self.fontComboBox.currentText(), int(self.spinBox.text()))
        self.item_search_window.show()

    def add_tab(self, tab_name):
        table = TableWidget(self)
        table.set_table()
        self.tabWidget.addTab(table, tab_name)
        self.table_list.append(table)
        if self.tabWidget.count() > 1:
            self.row_window.add_dropbox_items(
                self.row_window.select_tab_dropbox, tab_name)
            self.tab_items_list.append({})

    def remove_tab(self):
        if self.tabWidget.currentIndex() != 0:
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
            self.table_list.remove(
                self.table_list[self.tabWidget.currentIndex()])
            self.row_window.remove_dropbox_item(
                self.row_window.select_tab_dropbox, self.tabWidget.currentIndex()-1)

    def add_to_project_tab(self, list):
        self.add_row(0, list)

    def add_to_table(self, index, list):
        if index > -1:
            self.add_row(index+1, list)
            self.add_to_project_tab(list)
            if self.row_window.get_name_value_dict()[0] not in self.tab_items_list[index].keys():
                self.tab_items_list[index][self.row_window.get_name_value_dict(
                )[0]] = self.row_window.get_name_value_dict()[1]
                self.dropdown.addItem(self.row_window.get_name_value_dict(
                )[0])
            self.update_table_total_cost(index)
            self.row_window.close()

    def add_row(self, index, list):
        table = self.table_list[index].get_table_widget()
        row = table.rowCount()
        table.setRowCount(row+1)
        for i in range(table.columnCount()):
            item = QTableWidgetItem(list[i])
            table.setItem(row, i, item)
            table.item(row, i).setTextAlignment(
                QtCore.Qt.AlignmentFlag.AlignCenter)

    def remove_row_item(self):
        try:
            table = self.table_list[self.tabWidget.currentIndex(
            )].get_table_widget()
            table.removeRow(
                table.currentRow())
        except Exception as e:
            print("No row selected")

    def on_tab_changed(self, index):
        try:
            self.update_table_total_cost(index)
            self.show_dropbox_items()
            self.update_project_table()
        except:
            pass

    def update_table_total_cost(self, index):
        if index == self.tabWidget.currentIndex():
            table = self.table_list[index].get_table_widget()
            column = 5
            total_table_cost = sum([float(table.item(i, column).text()) for i in range(table
                                                                                       .rowCount())])
            self.label.setText(
                f'{self.tabWidget.tabText(index)} total cost : ')
            self.total_cost_label.setText(str(total_table_cost))

    def update_project_table(self):
        total_rows = sum([i.get_table_widget().rowCount()
                         for i in self.table_list[1:]])
        if total_rows != self.table_list[0].get_table_widget().rowCount():
            self.table_list[0].get_table_widget().setRowCount(total_rows)
            for i in range(1, len(self.table_list)):
                for row in self.table_list[i].get_table_widget().rowCount():
                    print(row)
                    #     # item = [self.table_list[i].get_table_widget().item(
                    #     #     row, col) for col in range(6)]
                    #     # self.add_row(0, item)

    def show_dropbox_items(self):
        try:
            self.dropdown.clear()
            if self.tabWidget.currentIndex() > 0:
                for k, v in self.tab_items_list[self.tabWidget.currentIndex()-1].items():
                    self.dropdown.addItem(k)
            else:
                for i in self.tab_items_list:
                    for k, v in i.items():
                        self.dropdown.addItem(k)
            self.dropdown.setCurrentIndex(-1)
        except:
            pass

    def change_table_styleSheet(self, e):
        for i in range(self.tabWidget.count()):
            font = self.table_list[i].font()
            font.setFamily(e)
            self.table_list[i].setFont(font)
        self.label.setFont(font)
        self.total_cost_label.setFont(font)

    def change_table_fontSize(self, e):
        for i in range(self.tabWidget.count()):
            font = self.table_list[i].font()
            font.setPointSize(int(e))
            self.table_list[i].setFont(font)
        self.label.setFont(font)
        self.total_cost_label.setFont(font)
