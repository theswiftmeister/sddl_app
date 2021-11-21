# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_tab_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class add_tab_dialog(object):
    def setupUi(self, add_tab_dialog):
        add_tab_dialog.setObjectName("add_tab_dialog")
        add_tab_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        add_tab_dialog.resize(400, 100)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            add_tab_dialog.sizePolicy().hasHeightForWidth())
        add_tab_dialog.setSizePolicy(sizePolicy)
        add_tab_dialog.setMinimumSize(QtCore.QSize(400, 100))
        add_tab_dialog.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        add_tab_dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(add_tab_dialog)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(add_tab_dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout.addWidget(self.label)
        self.input_tab_name = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.input_tab_name.sizePolicy().hasHeightForWidth())
        self.input_tab_name.setSizePolicy(sizePolicy)
        self.input_tab_name.setMinimumSize(QtCore.QSize(200, 0))
        self.input_tab_name.setMaximumSize(QtCore.QSize(200, 16777215))
        self.input_tab_name.setObjectName("input_tab_name")
        self.horizontalLayout.addWidget(self.input_tab_name)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(add_tab_dialog)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 35))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_ok = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_ok.sizePolicy().hasHeightForWidth())
        self.button_ok.setSizePolicy(sizePolicy)
        self.button_ok.setMinimumSize(QtCore.QSize(100, 0))
        self.button_ok.setMaximumSize(QtCore.QSize(100, 16777215))
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_2.addWidget(self.button_ok)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(add_tab_dialog)
        QtCore.QMetaObject.connectSlotsByName(add_tab_dialog)

    def retranslateUi(self, add_tab_dialog):
        _translate = QtCore.QCoreApplication.translate
        add_tab_dialog.setWindowTitle(_translate("add_tab_dialog", "Add Tab"))
        self.label.setText(_translate("add_tab_dialog", "Enter Tab Name : "))
        self.button_ok.setText(_translate("add_tab_dialog", "OK"))
