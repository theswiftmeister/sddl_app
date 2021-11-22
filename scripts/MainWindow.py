from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from guipy.main_window import MainWindow
from scripts.TabWindow import TabWindow
from scripts.RowWindow import RowWindow
from scripts.ItemSearchWindow import ItemSearchWindow
from scripts.TableWidget import TableWidget
from scripts.FileIO import FileIO


class MainWindow(QMainWindow, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        # Table list
        self.table_list = []

        # Unique items for searching for each table.
        self.tab_items_list = []

        # INIT
        self.tab_window = TabWindow(self)
        self.row_window = RowWindow(self)
        self.item_search_window = ItemSearchWindow(self)
        self.fileio = FileIO()

        # Menu Actions
        self.actionNew_Project.triggered.connect(self.new_project)

        # Button events
        self.btn_add_tab.clicked.connect(self.open_tab_window)
        self.btn_remove_tab.clicked.connect(self.remove_tab)
        self.btn_add_row.clicked.connect(lambda: self.open_row_window(True))
        self.btn_edit_row.clicked.connect(lambda: self.open_row_window(False))
        self.btn_remove_row.clicked.connect(self.remove_row_item)
        self.btn_search_item.clicked.connect(self.open_item_search_window)

        self.tabWidget.currentChanged.connect(lambda e: self.on_tab_changed(e))
        self.fontComboBox.textActivated.connect(
            lambda w: self.change_table_styleSheet(w))
        self.spinBox.textChanged.connect(
            lambda e: self.change_table_fontSize(e))

        self.add_tab("Project")

    def new_project(self):
        pass

    def open_tab_window(self):
        """OPEN NEW TAB WINDOW"""
        self.tab_window.show()

    def open_row_window(self, is_add_window):
        """OPEN NEW ROW WINDOW"""
        window = self.row_window
        is_first_tab = True if self.tabWidget.currentIndex() == 0 else False
        window.set_dropbox(
            window.select_tab_dropbox, is_first_tab, self.tabWidget.currentIndex()-1)

        try:
            window.btn_ok.clicked.disconnect()
        except:
            pass

        if is_add_window:
            if self.tabWidget.count() > 1:
                window.set_column_field_texts([""for i in range(5)])
                window.set_window_icon("./images/add_row.png")
                window.btn_ok.clicked.connect(lambda: self.add_to_table(
                    window.get_dropbox_current_index(window.select_tab_dropbox), window.column_texts()))
                window.btn_ok.clicked.connect(window.close)
                window.show()
        else:
            if self.tabWidget.currentIndex() != 0 and self.table_list[self.tabWidget.currentIndex()].currentRow() != -1:
                self.edit_row_window()
                window.set_window_icon("./images/edit_row.png")
                window.btn_ok.clicked.connect(
                    lambda: self.edit_row(window.column_texts()))
                window.btn_ok.clicked.connect(window.close)
                window.show()

    def open_item_search_window(self):
        """OPEN SEARCHED ITEMS WINDOW"""
        self.item_search_window.set_table(
            self.dropdown.currentText(), self.table_list[self.tabWidget.currentIndex()])
        self.item_search_window.set_table_font(
            self.fontComboBox.currentText(), int(self.spinBox.text()))
        self.item_search_window.show()

    def add_tab(self, tab_name):
        """ADD NEW TAB"""
        table = TableWidget(self)
        table.set_table()
        self.tabWidget.addTab(table, tab_name)
        self.table_list.append(table.get_table_widget())
        if self.tabWidget.count() > 1:
            self.row_window.add_dropbox_items(
                self.row_window.select_tab_dropbox, tab_name)
            self.tab_items_list.append({})

    def remove_tab(self):
        """REMOVE TAB"""
        if self.tabWidget.currentIndex() != 0:
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
            self.table_list.remove(
                self.table_list[self.tabWidget.currentIndex()])
            self.row_window.remove_dropbox_item(
                self.row_window.select_tab_dropbox, self.tabWidget.currentIndex())
            del self.tab_items_list[self.tabWidget.currentIndex()-1]
            self.update_project_table()

    def add_to_table(self, index, list):
        if index > -1:
            self.add_row(index+1, list)
            self.add_row(0, list)
            if self.row_window.get_name_value_dict()[0] not in self.tab_items_list[index].keys():
                self.tab_items_list[index][self.row_window.get_name_value_dict(
                )[0]] = self.row_window.get_name_value_dict()[1]
                self.dropdown.addItem(self.row_window.get_name_value_dict(
                )[0])
            self.update_table_total_cost(self.tabWidget.currentIndex())

    def add_row(self, index, list):
        table = self.table_list[index]
        row = table.rowCount()
        table.setRowCount(row+1)
        for i in range(table.columnCount()):
            self.add_row_item(table, row, i, list[i])

    def edit_row_window(self):
        try:
            table = self.table_list[self.tabWidget.currentIndex(
            )]

            self.row_window.set_column_field_texts(
                [table.item(table.currentRow(), col).text() for col in range(table.columnCount())][1:])
            self.row_window.show()
        except Exception as e:
            print("No row selected", e)

    def edit_row(self, list):
        table = self.table_list[self.tabWidget.currentIndex()]
        row = table.currentRow()
        for i in range(self.table_list[self.tabWidget.currentIndex()].columnCount()):
            self.add_row_item(table, row, i, list[i])
        self.update_project_table()
        self.update_table_total_cost(self.tabWidget.currentIndex())

    def add_row_item(self, table, row, col, text):
        item = QTableWidgetItem(text)
        table.setItem(row, col, item)
        table.item(row, col).setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

    def remove_row_item(self):
        try:
            table = self.table_list[self.tabWidget.currentIndex(
            )]
            if self.tabWidget.currentIndex() != 0:
                table.removeRow(
                    table.currentRow())
                self.update_project_table()
        except Exception as e:
            print("No row selected", e)

    def update_project_table(self):
        self.table_list[0].setRowCount(0)
        for i in range(1, len(self.table_list)):
            for row in range(self.table_list[i].rowCount()):
                list = [self.table_list[i].item(row, col).text(
                ) for col in range(self.table_list[i].columnCount())]
                self.add_row(0, list)

    def on_tab_changed(self, index):
        try:
            self.update_table_total_cost(index)
            self.show_dropbox_items()
        except:
            pass

    def update_table_total_cost(self, index):
        table = self.table_list[index]
        column = 5
        total_table_cost = sum([float(table.item(i, column).text()) for i in range(table
                                                                                   .rowCount())])
        self.label.setText(
            f'{self.tabWidget.tabText(index)} total cost : ')
        self.total_cost_label.setText(str(total_table_cost))

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
