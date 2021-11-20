# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warning_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class warning_dialog(object):
    def setupUi(self, WarningDialogBox):
        WarningDialogBox.setObjectName("WarningDialogBox")
        WarningDialogBox.setWindowModality(QtCore.Qt.ApplicationModal)
        WarningDialogBox.resize(400, 110)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            WarningDialogBox.sizePolicy().hasHeightForWidth())
        WarningDialogBox.setSizePolicy(sizePolicy)
        WarningDialogBox.setMinimumSize(QtCore.QSize(400, 110))
        WarningDialogBox.setMaximumSize(QtCore.QSize(400, 110))
        font = QtGui.QFont()
        font.setPointSize(12)
        WarningDialogBox.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(WarningDialogBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_frame = QtWidgets.QFrame(WarningDialogBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.text_frame.setFont(font)
        self.text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text_frame.setObjectName("text_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.text_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.warning_text_label = QtWidgets.QLabel(self.text_frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.warning_text_label.setFont(font)
        self.warning_text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_text_label.setObjectName("warning_text_label")
        self.verticalLayout_2.addWidget(self.warning_text_label)
        self.verticalLayout.addWidget(self.text_frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(WarningDialogBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(WarningDialogBox)
        self.buttonBox.accepted.connect(
            WarningDialogBox.accept)  # type: ignore
        self.buttonBox.rejected.connect(
            WarningDialogBox.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WarningDialogBox)

    def retranslateUi(self, WarningDialogBox):
        _translate = QtCore.QCoreApplication.translate
        WarningDialogBox.setWindowTitle(
            _translate("WarningDialogBox", "Warning"))
        self.warning_text_label.setText(
            _translate("WarningDialogBox", "#WarningText"))