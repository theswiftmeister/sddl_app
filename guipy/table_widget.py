# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class table_widget(object):
    def setupUi(self, tab_table):
        tab_table.setObjectName("tab_table")
        tab_table.resize(604, 493)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        tab_table.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(tab_table)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(tab_table)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(0)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(tab_table)
        QtCore.QMetaObject.connectSlotsByName(tab_table)

    def retranslateUi(self, tab_table):
        _translate = QtCore.QCoreApplication.translate
        tab_table.setWindowTitle(_translate("tab_table", "Form"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("tab_table", "Date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("tab_table", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("tab_table", "Unit"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("tab_table", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("tab_table", "Rate"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("tab_table", "Total"))
