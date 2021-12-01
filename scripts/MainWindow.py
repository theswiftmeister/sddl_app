from os import close
from typing import final
from PyQt5 import QtCore, QtGui
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter, QPrintDialog
from PyQt5.QtWidgets import QDialogButtonBox, QFileDialog, QMainWindow, QTableWidgetItem
from guipy.main_window import MainWindow
from scripts.Row import Row
from scripts.TabWindow import TabWindow
from scripts.RowWindow import RowWindow
from scripts.ItemSearchWindow import ItemSearchWindow
from scripts.WarningDialog import WarningWindow
from scripts.QuitDialog import QuitDialog
from scripts.Table import Table
from scripts.FileIO import FileIO
import getpass

DIR = f"C:\\Users\\{getpass.getuser()}\\Documents"
FILE_TYPE = ".sdb"
SAVE_FILE_NAME = "data_sav"


class MainWindow(QMainWindow, MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.is_save_prompt = False

        self.current_project_dir = ""
        self.project_name = ""

        self.table_list = []

        self.table_data = []

        self.deleted_items = []

        # INIT
        self.tab_window = TabWindow(self)
        self.row_window = RowWindow(self)
        self.item_search_window = ItemSearchWindow(self)
        self.warn_window = WarningWindow()
        self.quit_window = QuitDialog(self)
        self.fileio = FileIO()

        # Menu Actions
        self.actionNew_Project.triggered.connect(
            lambda: self.new_project("New Project"))
        self.actionLoad_Project.triggered.connect(self.load_project)
        self.actionSave_Project.triggered.connect(self.save_project)
        self.actionSave_As.triggered.connect(self.save_as_project)
        self.print_file.triggered.connect(lambda: self.print_preview_widget(
            self.table_list[self.tabWidget.currentIndex()], self.windowTitle(), self.total_cost_label.text()))
        self.menu_undo.triggered.connect(self.undo)
        self.actionQuit.triggered.connect(self.close)

        # Button events
        self.btn_add_tab.clicked.connect(self.open_tab_window)
        self.btn_remove_tab.clicked.connect(lambda: self.open_warn_window(
            f"Are you sure you want to delete {self.tabWidget.tabText(self.tabWidget.currentIndex())}?", ["yes", "no"], self.remove_tab))
        self.btn_add_row.clicked.connect(lambda: self.open_row_window(True))
        self.btn_edit_row.clicked.connect(lambda: self.open_row_window(False))
        self.btn_remove_row.clicked.connect(self.remove_row_item)
        self.btn_search_item.clicked.connect(self.open_item_search_window)
        self.btn_view_whole_project.clicked.connect(self.view_whole_project)

        self.tabWidget.currentChanged.connect(lambda e: self.on_tab_changed(e))
        self.fontComboBox.textActivated.connect(
            lambda e: self.change_table_styleSheet(e))
        self.spinBox.textChanged.connect(
            lambda e: self.change_table_fontSize(e))

    def open_warn_window(self, text, btn_names, accept_func, reject_func=None):
        """

        """
        warn = self.warn_window
        try:
            warn.buttonBox.accepted.disconnect()
            warn.buttonBox.rejected.disconnect()
        except:
            pass

        warn.buttonBox.accepted.connect(accept_func)
        warn.buttonBox.accepted.connect(warn.close)
        warn.buttonBox.rejected.connect(
            warn.close if reject_func == None else reject_func)
        warn.set_window(text, btn_names)
        warn.show()

    def closeEvent(self, e: QtGui.QCloseEvent) -> None:
        try:
            if self.table_data != self.fileio.load(self.current_project_dir):
                self.quit_window.show()
                if not self.is_save_prompt:
                    e.ignore()
            else:
                e.accept()
        except Exception as e:
            print(e)

    def reset_project(self):
        self.tabWidget.clear()
        self.table_data.clear()
        self.table_list.clear()
        self.deleted_items.clear()
        for i in self.menu_clickables:
            i.setEnabled(True)

    def new_project(self, window_title):
        dialog = QFileDialog.getSaveFileName(
            self, window_title, DIR if not self.current_project_dir else self.current_project_dir)
        if dialog[0]:
            try:
                path = QtCore.QFileInfo(dialog[0])
                self.project_name = path.baseName()
                self.fileio.mkdir(path.filePath())
                self.fileio.create_project_files(
                    [f"{SAVE_FILE_NAME}"], path.filePath(), FILE_TYPE)
                self.current_project_dir = f"{path.filePath()}/{SAVE_FILE_NAME}{FILE_TYPE}"
                self.setWindowTitle(f"SDDL-{self.project_name}")
                self.reset_project()
            except Exception as e:
                print(e)
                self.open_warn_window(
                    "Invalid Directory, no project was created.", ["ok"], lambda *args: None)

    def load_project(self):
        dialog = QFileDialog.getOpenFileName(
            self, "Select a File to Open", DIR if not self.current_project_dir else self.current_project_dir, "*.sdb")
        if dialog[0]:
            try:
                self.reset_project()
                self.table_data = self.fileio.load(
                    dialog[0])
                print(self.table_data)
                self.current_project_dir = dialog[0]
                self.project_name = (QtCore.QFileInfo(QtCore.QFileInfo(
                    dialog[0]).absolutePath()).baseName())
                self.setWindowTitle(
                    f"SDDL-{self.project_name}")

                for id, i in enumerate(self.table_data):
                    self.create_tab(i["name"], id)
                    for rows in range(len(i["rows"])):
                        self.add_row(id, i["rows"][rows])
                self.on_tab_changed(self.tabWidget.currentIndex())
            except Exception as e:
                print(e)

    def save_project(self):
        try:
            if self.table_data != self.fileio.load(self.current_project_dir):
                print(self.table_data)
                self.fileio.save(self.current_project_dir, self.table_data)
            else:
                print("No changes was made.")
        except:
            print("File not found!!")
            self.open_warn_window(
                "File not found!!", ["ok"], lambda *args: None)

    def save_as_project(self):
        self.new_project("Save as new")
        self.save_project()

    def open_tab_window(self):
        """Opens tab window."""
        self.tab_window.show()

    def open_row_window(self, is_new):
        """Open new row window."""
        try:
            window = self.row_window
            try:
                # disconnect button event
                window.btn_ok.clicked.disconnect()
            except:
                pass

            tab_widget = self.tabWidget
            # Clears window
            window.reset()
            # Sets tab dropbox items
            tab_names = [data["name"] for data in self.table_data]
            window.add_dropbox_items(window.select_tab_dropbox, tab_names)

            # Sets item dropbox items
            tab_items = [*self.table_data[tab_widget.currentIndex()]
                         ["unit"].keys()]
            window.add_dropbox_items(window.select_item_dropbox, tab_items)

            if tab_widget.currentIndex() > -1:
                # Sets combo box index and disables
                window.set_combo_box(window.select_tab_dropbox,
                                     tab_widget.currentIndex(), False)
                if is_new:
                    self.row_window_config(lambda: self.add_row_item(
                        window.select_tab_dropbox.currentIndex(), window.get_input_field_values()), "Add new row window", "./images/add_row.png")
                else:
                    try:
                        # Current selected row in current table.
                        current_row = self.table_list[self.tabWidget.currentIndex(
                        )].current_row()
                        if current_row > -1:
                            row_texts = self.table_data[tab_widget.currentIndex(
                            )]["rows"][current_row][1:]

                            # Sets input field as per row cell values.
                            window.set_input_field_values(row_texts)

                            # Number ordinals for rows starting from 0 and displayed as current row + 1.
                            ordinal = {"1": "st", "2": "nd", "3": "rd"}[str(current_row+1)] if str(
                                current_row+1) in {"1": "st", "2": "nd", "3": "rd"}.keys() else " th"

                            # Sets window title
                            window_title = f"Edit {current_row+1}{ordinal}-row item"
                            self.row_window_config(
                                lambda: self.edit_row_item(current_row, window.get_input_field_values()), window_title, "./images/edit_row.png")
                    except Exception as e:
                        print(e)
        except:
            self.open_warn_window(
                "No tabs available. Please create one to continue...", ["ok"], lambda *args: None)

    def row_window_config(self, func, window_title, path):
        # Sets button ok event
        self.row_window.btn_ok.clicked.connect(func)
        # Sets window title
        self.row_window.setWindowTitle(window_title)
        # Sets window icon
        self.row_window.set_window_icon(path,)
        # open window
        self.row_window.show()

    def open_item_search_window(self):
        """OPEN SEARCHED ITEMS WINDOW"""
        try:
            if self.dropdown.currentIndex() > -1:
                self.item_search_window.set_table(
                    self.dropdown.currentText(), self.table_list[self.tabWidget.currentIndex()].get_table())
                self.item_search_window.set_table_font(
                    self.fontComboBox.currentText(), int(self.spinBox.text()))
                self.item_search_window.show()
            else:
                self.open_warn_window(
                    "No search item is selected.", ['ok'], lambda *args: None)
        except Exception as e:
            print(e)

    def add_tab(self, tab_name):
        """(function)
        Checks whether tab_name in data listm if then calls create_tab function.
        Params :
                tab_name : name of tab"""
        # List of tab names.
        current_tab_names = [data["name"] for data in self.table_data]

        # Checks if tab name is already present in data list  name key dict.
        if tab_name and tab_name not in current_tab_names:
            self.create_tab(tab_name, self.tabWidget.count())
            self.tab_window.close()

    def create_tab(self, tab_name: str, index: int):
        """(function)
        Creates Table object and inserts to tab.\n
        Checks whether index is greater than zero, if then add a data dictionary to project data list.
        Params :
                tab_name : name of tab
                index : index of insertion."""

        # Create Table
        table = Table()

        # Insert Tab
        self.tabWidget.insertTab(index, table.create_table(), tab_name)

        # Append to data list if index is greater than zero.
        self.table_list.append(table)

        if tab_name not in [data["name"] for data in self.table_data]:
            self.table_data.append(
                {"name": tab_name, "unit": {}, "rows": []})

    def remove_tab(self):
        """ (function)
        Removes current selected tab from tab widget."""
        try:
            # Current selected tab index
            index = self.tabWidget.currentIndex()
            # Append to deleted items for undo.
            table: Table = self.table_list[index]
            self.deleted_items.append(
                {"index": index, "name": self.tabWidget.tabText(index), "type": table, "data": self.table_data[index]})
            # Removes current tab
            self.tabWidget.removeTab(index)
            # Removes from data list at index.
            self.table_data.pop(index)
            # Removes table from table list at index.
            self.table_list.pop(index)
        except:
            pass

    def add_row_item(self, index: int, list: list):
        """(function)
        Insert row to table.
        Params :
                index : table data index
                list : row input field value text list """
        # Checks whether if fields have values.
        if all([True if list[i] else False for i in range(len(list))]):

            # Add row to table.
            self.add_row(index, list)
            self.on_tab_changed(index)

            # Append to table data only if entered new, but not loaded from save file.
            self.table_data[index]["rows"].append(list)
            # Close row window
            self.row_window.close()

        else:
            for i in self.row_window.get_input_field():
                if not i.text():
                    i.setPlaceholderText("Required....")

    def add_row(self, index, list: list):
        """(function)
        Add row to table at index.
        Params:
                index : current tab index.
                list : list of field values.
        """
        table = self.table_list[index]

        # Create Row object
        row = Row(list)

        # Call add_row function from table object
        table.add_row(row)

        # Get name text from cell with name
        name_text = row.get_name_cell().get_text()
        unit_text = row.get_unit_cell().get_text()

        # Checking whether name in dict
        if name_text not in self.get_unit_list(index):
            # Add name,unit as key,value pair in dict.
            self.table_data[index]["unit"][name_text] = unit_text

    def edit_row_item(self, index, data_list):
        """(function)
        Edit row to table at index.
        """
        if all([True if data_list[i] else False for i in range(len(data_list))]):
            table: Table = self.table_list[self.tabWidget.currentIndex()]
            table.edit_row(index, data_list)
            self.table_data[self.tabWidget.currentIndex()
                            ]["unit"][data_list[1]] = data_list[2]
            self.table_data[self.tabWidget.currentIndex()
                            ]["rows"][index] = data_list
            self.on_tab_changed(self.tabWidget.currentIndex())
            # Close row window
            self.row_window.close()
        else:
            for i in self.row_window.get_input_field():
                if not i.text():
                    i.setPlaceholderText("Required....")

    def insert_row_item(self, index: int, row: Row):
        """(function)
        Inserts row to table at index.
        """
        table: Table = self.table_list[self.tabWidget.currentIndex()]
        table.insert_row(index, row)
        self.table_data[self.tabWidget.currentIndex()
                        ]["rows"].insert(index, row.get_row_texts())

    def remove_row_item(self):
        """(function)
        Removes row to table at index.
        """
        try:
            table: Table = self.table_list[self.tabWidget.currentIndex(
            )]
            if table.current_row() != -1:

                row: Row = table.get_rows()[table.current_row()]
                # Appends to deleted items list.
                self.deleted_items.append(
                    {"index": table.current_row(), "type": row})

                table.delete_row(table.current_row())
                self.table_data[self.tabWidget.currentIndex()
                                ]["rows"].pop(table.current_row())
            else:
                self.open_warn_window(
                    "No rows selected.", ['ok'], lambda *args: None)
        except:
            pass

    def undo(self):
        """(function)
        Undo last deleted item.
        """
        try:
            object = self.deleted_items[-1]
            if type(object["type"]) == Table:
                self.tabWidget.insertTab(
                    object["index"], object["type"].get_table(), object["name"])
                self.table_data.insert(object["index"], object["data"])
                self.table_list.insert(
                    object["index"], object["type"])
            elif type(object["type"]) == Row:
                self.insert_row_item(object["index"], object["type"])
            self.deleted_items.pop()
            self.on_tab_changed(self.tabWidget.currentIndex())
        except Exception as e:
            print(e)

    def on_tab_changed(self, index):
        """(function)
        Called when tab is changed.
        """
        try:
            if index > -1:
                self.update_table_total_cost(index)
                self.show_dropbox_items()
        except Exception as e:
            print(e)

    def update_table_total_cost(self, index):
        """(function)
        Updates total cost.
        """
        table = self.table_list[index].get_table()
        column = 5
        total_table_cost = format(sum([float(table.item(i, column).text()) for i in range(table
                                                                                          .rowCount())]), ".2f")
        self.label.setText(
            f'{self.tabWidget.tabText(index)} total cost : ')
        self.total_cost_label.setText(total_table_cost)

    def show_dropbox_items(self):
        """(function)
        Shows dropdown items from current tab index.
        """
        try:
            self.dropdown.clear()
            for key, value in self.table_data[self.tabWidget.currentIndex()]["unit"].items():
                self.dropdown.addItem(key)
            self.dropdown.setCurrentIndex(-1)
        except:
            pass

    def view_whole_project(self):
        """OPEN SEARCHED ITEMS WINDOW"""
        try:
            table_items = []
            for i in self.table_data:
                for j in i["rows"]:
                    table_items.append(j)
            print(table_items)
            self.item_search_window.set_whole_project(
                "Project Table", table_items)
            self.item_search_window.set_table_font(
                self.fontComboBox.currentText(), int(self.spinBox.text()))
            self.item_search_window.show()
        except Exception as e:
            print(e)

    def get_unit_dict(self):
        return self.table_data[self.tabWidget.currentIndex()]["unit"]

    def get_unit_list(self, index):
        tab_item_dict = self.table_data[index]["unit"]
        return [key for key, value in tab_item_dict.items()]

    def change_table_styleSheet(self, e):
        try:
            for i in range(self.tabWidget.count()):
                font = self.table_list[i].get_table().font()
                font.setFamily(e)
                self.table_list[i].get_table().setFont(font)
            self.label.setFont(font)
            self.total_cost_label.setFont(font)
        except:
            pass

    def change_table_fontSize(self, e):
        try:
            for i in range(self.tabWidget.count()):
                font = self.table_list[i].get_table().font()
                font.setPointSize(int(e))
                self.table_list[i].get_table().setFont(font)
            self.label.setFont(font)
            self.total_cost_label.setFont(font)
        except:
            pass

    def set_is_save_prompt(self, bool):
        self.is_save_prompt = bool

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
