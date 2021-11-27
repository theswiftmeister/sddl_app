from PyQt5 import QtCore, QtGui
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter, QPrintDialog
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QTableWidgetItem
from guipy.main_window import MainWindow
from scripts.TabWindow import TabWindow
from scripts.RowWindow import RowWindow
from scripts.ItemSearchWindow import ItemSearchWindow
from scripts.WarningDialog import WarningWindow
from scripts.TableWidget import TableWidget
from scripts.FileIO import FileIO
from collections import ChainMap


DIR = "./"
FILE_TYPE = ".sdb"
TAB_ITEMS_FILE_NAME = "_doc"
TABLE_ROWS_FILE_NAME = "_doc2"


class MainWindow(QMainWindow, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.current_project_dir = ""

        # Table list
        self.table_list = []

        # Unique items for searching for each table.
        self.tab_items_list = []

        # Rows for each table.
        self.tab_table_list = []

        # INIT
        self.tab_window = TabWindow(self)
        self.row_window = RowWindow(self)
        self.item_search_window = ItemSearchWindow(self)
        self.warn_window = WarningWindow()
        self.fileio = FileIO()

        # Menu Actions
        self.actionNew_Project.triggered.connect(
            lambda: self.new_project("New Project"))
        self.actionLoad_Project.triggered.connect(self.load_project)
        self.actionSave_Project.triggered.connect(self.save_project)
        self.actionSave_As.triggered.connect(self.save_as_project)
        self.print_file.triggered.connect(lambda: self.print_preview_widget(
            self.table_list[self.tabWidget.currentIndex()], self.windowTitle(), self.total_cost_label.text()))
        self.actionQuit.triggered.connect(self.close)

        # Button events
        self.btn_add_tab.clicked.connect(self.open_tab_window)
        self.btn_remove_tab.clicked.connect(self.remove_tab)
        self.btn_add_row.clicked.connect(lambda: self.open_row_window(True))
        self.btn_edit_row.clicked.connect(lambda: self.open_row_window(False))
        self.btn_remove_row.clicked.connect(self.remove_row_item)
        self.btn_search_item.clicked.connect(self.open_item_search_window)

        self.tabWidget.currentChanged.connect(lambda e: self.on_tab_changed(e))
        self.fontComboBox.textActivated.connect(
            lambda e: self.change_table_styleSheet(e))
        self.spinBox.textChanged.connect(
            lambda e: self.change_table_fontSize(e))

    def reset_project(self):
        self.tabWidget.clear()
        self.table_list.clear()
        self.create_table("Project")
        for i in self.menu_clickables:
            i.setEnabled(True)

    def new_project(self, window_title):
        dialog = QFileDialog.getSaveFileName(
            self, window_title, DIR)
        if dialog[0]:
            self.reset_project()
            path = QtCore.QFileInfo(dialog[0])
            self.fileio.mkdir(path.filePath())
            self.fileio.create_project_files(
                [TAB_ITEMS_FILE_NAME, TABLE_ROWS_FILE_NAME], path.filePath(), FILE_TYPE)
            self.current_project_dir = path.filePath()
            self.setWindowTitle(f"SDDL-{path.fileName()}")

    def load_project(self):
        dialog = QFileDialog.getExistingDirectory(
            self, "Select a Project folder", DIR)
        if dialog:
            self.reset_project()
            files = self.fileio.get_project_files(dialog)
            if [f'{TAB_ITEMS_FILE_NAME}{FILE_TYPE}', f'{TABLE_ROWS_FILE_NAME}{FILE_TYPE}'] == files:
                self.tab_items_list = self.fileio.load(
                    dialog, TAB_ITEMS_FILE_NAME, FILE_TYPE)
                self.tab_table_list = self.fileio.load(
                    dialog, TABLE_ROWS_FILE_NAME, FILE_TYPE)
                self.current_project_dir = dialog
                self.setWindowTitle(
                    f"SDDL-{QtCore.QFileInfo(dialog).fileName()}")

                for id, i in enumerate(self.tab_table_list):
                    self.create_table(i["name"])
                    for rows in range(len(i["rows"])):
                        self.add_row(id+1, i["rows"][rows])
                self.update_project_table()
                self.on_tab_changed(0)
            else:
                self.open_warn_window("Invalid project folder.", ['ok'])

    def save_project(self):
        lists = [self.tab_items_list, self.tab_table_list]
        for i, file_name in enumerate([TAB_ITEMS_FILE_NAME, TABLE_ROWS_FILE_NAME]):
            if lists[i] != self.fileio.load(self.current_project_dir, file_name, FILE_TYPE):
                self.fileio.save(self.current_project_dir,
                                 file_name, FILE_TYPE, lists[i])

    def save_as_project(self):
        self.new_project("Save as new")
        self.save_project()

    def open_tab_window(self):
        """OPEN NEW TAB WINDOW"""
        self.tab_window.show()

    def open_row_window(self, is_add_window):
        """OPEN NEW ROW WINDOW"""
        window = self.row_window
        is_first_tab = True if self.tabWidget.currentIndex() == 0 else False
        try:
            window.btn_ok.clicked.disconnect()
        except:
            pass

        if is_add_window:
            if self.tabWidget.count() > 1:
                def btn_func(): return self.add_to_table(
                    window.get_dropbox_current_index(window.select_tab_dropbox), window.column_texts())

                self.row_window_config(
                    "Add Row", [""for i in range(5)], "./images/add_row.png", btn_func)
            else:
                self.open_warn_window(
                    "No table is available. Please add a new tab.", ['ok'])
        else:
            tab_index = self.tabWidget.currentIndex()
            table = self.table_list[tab_index]
            if tab_index != 0 and table.currentRow() != -1:
                def btn_func(): return self.edit_row(window.column_texts())

                row_column_texts = [table.item(table.currentRow(), col).text(
                ) for col in range(table.columnCount())][1:]

                self.row_window_config(
                    "Edit Row", row_column_texts, "./images/edit_row.png", btn_func)
            else:
                self.open_warn_window(
                    "No rows selected." if tab_index != 0 else "Cannot edit rows in Project table.", ['ok'])

        window.set_dropbox(
            window.select_tab_dropbox, is_first_tab, self.tabWidget.currentIndex()-1)

        window.set_dropbox_current_index(
            window.select_item_dropbox, list(ChainMap(*self.tab_items_list)) if self.tabWidget.currentIndex() == 0 else self.tab_items_list[self.tabWidget.currentIndex()-1].keys())

        window.select_item_dropbox.setCurrentIndex(-1)

    def row_window_config(self, window_title, columns_text, image_url, btn_func, other_func=None):
        window = self.row_window
        window.setWindowTitle(window_title)
        window.set_column_field_texts(columns_text)
        window.set_window_icon(image_url)
        window.set_dropbox_current_index(
            window.select_tab_dropbox, self.get_tab_item_texts())
        window.btn_ok.clicked.connect(btn_func)
        if other_func != None:
            other_func()
        window.show()

    def open_item_search_window(self):
        """OPEN SEARCHED ITEMS WINDOW"""
        if self.dropdown.currentIndex() != -1:
            self.item_search_window.set_table(
                self.dropdown.currentText(), self.table_list[self.tabWidget.currentIndex()])
            self.item_search_window.set_table_font(
                self.fontComboBox.currentText(), int(self.spinBox.text()))
            self.item_search_window.show()
        else:
            self.open_warn_window(
                "No search item is selected.", ['ok'])

    def add_tab(self, tab_name):
        """ADD NEW TAB"""
        if tab_name:
            self.create_table(tab_name)
            if self.tabWidget.count() > 1:
                self.tab_items_list.append({})
                self.tab_table_list.append({"name": tab_name, "rows": []})
            self.tab_window.close()
        else:
            self.open_warn_window(
                "Table name cannot be empty.", ['ok'])

    def create_table(self, tab_name):
        table = TableWidget(self)
        table.set_table()
        self.tabWidget.addTab(table, tab_name)
        self.table_list.append(table.get_table_widget())

    def remove_tab(self):
        """REMOVE TAB"""
        if self.tabWidget.currentIndex() != 0:
            del self.tab_items_list[self.tabWidget.currentIndex()-1]
            del self.table_list[self.tabWidget.currentIndex()]
            del self.tab_table_list[self.tabWidget.currentIndex()-1]
            self.update_project_table()
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
        else:
            self.open_warn_window(
                "Project tab cannot be deleted.", ['ok'])

    def add_to_table(self, index, list):
        if all([True if list[i] else False for i in range(len(list))]):
            if index > -1:
                self.add_row(index+1, list)
                self.tab_table_list[index]["rows"].append(list)
                self.add_row(0, list)
                if self.row_window.get_name_value_dict()[0] not in self.tab_items_list[index].keys():
                    self.tab_items_list[index][self.row_window.get_name_value_dict(
                    )[0]] = self.row_window.get_name_value_dict()[1]
                    self.dropdown.addItem(self.row_window.get_name_value_dict(
                    )[0])
                self.update_table_total_cost(self.tabWidget.currentIndex())
                self.row_window.close()
            else:
                self.open_warn_window(
                    "Add to tab : Cannot be empty.", ['ok'])
        else:
            for i in self.row_window.get_column_field_texts():
                if not i.text():
                    i.setPlaceholderText("Required....")

    def add_row(self, index, list):
        table = self.table_list[index]
        row = table.rowCount()
        table.setRowCount(row+1)
        for i in range(table.columnCount()):
            self.add_row_item(table, row, i, list[i])

    def edit_row(self, list):
        table = self.table_list[self.tabWidget.currentIndex()]
        row = table.currentRow()
        self.tab_table_list[self.tabWidget.currentIndex() -
                            1]["rows"][row] = list
        for i in range(self.table_list[self.tabWidget.currentIndex()].columnCount()):
            self.add_row_item(table, row, i, list[i])
        self.row_window.close()
        self.update_project_table()
        self.update_table_total_cost(self.tabWidget.currentIndex())

    def add_row_item(self, table, row, col, text):
        item = QTableWidgetItem(text)
        table.setItem(row, col, item)
        table.item(row, col).setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)

    def remove_row_item(self):
        table = self.table_list[self.tabWidget.currentIndex(
        )]
        if self.tabWidget.currentIndex() != 0:
            if table.currentRow() != -1:
                table.removeRow(
                    table.currentRow())
                del self.tab_table_list[self.tabWidget.currentIndex() -
                                        1]["rows"][table.currentRow()]

                self.update_project_table()
            else:
                self.open_warn_window(
                    "No rows selected.", ['ok'])
        else:
            self.open_warn_window(
                "Cannot delete rows from Project Tab.", ['ok'])

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
        total_table_cost = format(sum([float(table.item(i, column).text()) for i in range(table
                                                                                          .rowCount())]), ".2f")
        self.label.setText(
            f'{self.tabWidget.tabText(index)} total cost : ')
        self.total_cost_label.setText(total_table_cost)

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

    def get_tab_item_texts(self):
        return [self.tabWidget.tabText(i) for i in range(1, self.tabWidget.count())]

    def get_name_value_dict(self):
        return self.tab_items_list

    def open_warn_window(self, text, btn_names):
        """
        Standard Button selection codes:\n
        ok -> StandardButton.Ok
        """
        warn = self.warn_window
        warn.set_window(text, btn_names)
        warn.show()

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

    def print_widget(self, current_table, title, text):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec() == QPrintDialog.Accepted:
            self.print_doc(printer, current_table, title, text)

    def print_preview_widget(self, current_table, title, text):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintPreviewDialog(printer, self)
        dialog.paintRequested.connect(
            lambda: self.print_doc(printer, current_table, title, text))
        dialog.exec_()

    def print_doc(self, printer, current_table, title, text):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        font = current_table.font()
        self.insert_line_text(
            cursor, 0, title, 16, QtCore.Qt.AlignmentFlag.AlignCenter)
        cursor.movePosition(QtGui.QTextCursor.Down)

        table = cursor.insertTable(
            current_table.rowCount()+1, current_table.columnCount(), self.table_format(1))

        for id, c in enumerate([current_table.horizontalHeaderItem(i).text() for i in range(current_table.columnCount())]):
            table.cellAt(0, id).firstCursorPosition().setBlockFormat(
                self.print_text_align(QtCore.Qt.AlignmentFlag.AlignCenter))
            cursor.insertText(c, self.char_format(
                font.family(), font.pointSize()))
            cursor.movePosition(QtGui.QTextCursor.NextCell)

        for row in range(table.rows()-1):
            for col in range(table.columns()):
                table.cellAt(row+1, col).firstCursorPosition().setBlockFormat(
                    self.print_text_align(QtCore.Qt.AlignmentFlag.AlignCenter))
                cursor.insertText(
                    current_table.item(row, col).text(), self.char_format(
                        font.family(), font.pointSize()))
                cursor.movePosition(QtGui.QTextCursor.NextCell)

        cursor.movePosition(QtGui.QTextCursor.Down)
        self.insert_line_text(
            cursor, 0, f"Sub-Total : Tk. {text} /-", font.pointSize() * 1.2, QtCore.Qt.AlignmentFlag.AlignRight)

        document.print_(printer)

    def insert_line_text(self, cursor, border_size, text, font_size, align):
        table = cursor.insertTable(
            1, 1, self.table_format(border_size))
        table.cellAt(0, 0).firstCursorPosition().setBlockFormat(
            self.print_text_align(align))
        cursor.insertText(text,
                          self.char_format("Roboto", font_size))

    def table_format(self, border_size):
        tableFormat = QtGui.QTextTableFormat()
        tableFormat.setBorder(border_size)
        tableFormat.setBorderStyle(3)
        tableFormat.setCellSpacing(0)
        tableFormat.setTopMargin(0)
        tableFormat.setCellPadding(4)
        tableFormat.setWidth(QtGui.QTextLength(
            QtGui.QTextLength.PercentageLength, 100))
        tableFormat.setHeight(QtGui.QTextLength(
            QtGui.QTextLength.PercentageLength, 100))
        return tableFormat

    def char_format(self, font_family, point_size):
        charFormat = QtGui.QTextCharFormat()
        charFormat.setFontFamily(font_family)
        charFormat.setFontPointSize(point_size)

        return charFormat

    def print_text_align(self, align):
        alignment = QtGui.QTextBlockFormat()
        alignment.setAlignment(align)
        return alignment
