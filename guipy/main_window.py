# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/db.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(6, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_tab_btns = QtWidgets.QHBoxLayout()
        self.layout_tab_btns.setSpacing(2)
        self.layout_tab_btns.setObjectName("layout_tab_btns")
        self.btn_add_tab = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_add_tab.sizePolicy().hasHeightForWidth())
        self.btn_add_tab.setSizePolicy(sizePolicy)
        self.btn_add_tab.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_add_tab.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.btn_add_tab.setFont(font)
        self.btn_add_tab.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./images/add_tab.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_tab.setIcon(icon1)
        self.btn_add_tab.setIconSize(QtCore.QSize(36, 36))
        self.btn_add_tab.setFlat(True)
        self.btn_add_tab.setObjectName("btn_add_tab")
        self.layout_tab_btns.addWidget(self.btn_add_tab)
        self.btn_remove_tab = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_remove_tab.sizePolicy().hasHeightForWidth())
        self.btn_remove_tab.setSizePolicy(sizePolicy)
        self.btn_remove_tab.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_remove_tab.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_remove_tab.setFont(font)
        self.btn_remove_tab.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./images/remove_tab.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove_tab.setIcon(icon2)
        self.btn_remove_tab.setIconSize(QtCore.QSize(36, 36))
        self.btn_remove_tab.setFlat(True)
        self.btn_remove_tab.setObjectName("btn_remove_tab")
        self.layout_tab_btns.addWidget(self.btn_remove_tab)
        self.horizontalLayout.addLayout(self.layout_tab_btns)
        spacerItem = QtWidgets.QSpacerItem(
            20, 37, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.layout_row_btns = QtWidgets.QHBoxLayout()
        self.layout_row_btns.setSpacing(2)
        self.layout_row_btns.setObjectName("layout_row_btns")
        self.btn_add_row = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_add_row.sizePolicy().hasHeightForWidth())
        self.btn_add_row.setSizePolicy(sizePolicy)
        self.btn_add_row.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_add_row.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_row.setFont(font)
        self.btn_add_row.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./images/add_row.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_row.setIcon(icon3)
        self.btn_add_row.setIconSize(QtCore.QSize(36, 36))
        self.btn_add_row.setFlat(True)
        self.btn_add_row.setObjectName("btn_add_row")
        self.layout_row_btns.addWidget(self.btn_add_row)
        self.btn_edit_row = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_edit_row.sizePolicy().hasHeightForWidth())
        self.btn_edit_row.setSizePolicy(sizePolicy)
        self.btn_edit_row.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_edit_row.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_edit_row.setFont(font)
        self.btn_edit_row.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./images/edit_row.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_row.setIcon(icon4)
        self.btn_edit_row.setIconSize(QtCore.QSize(36, 36))
        self.btn_edit_row.setFlat(True)
        self.btn_edit_row.setObjectName("btn_edit_row")
        self.layout_row_btns.addWidget(self.btn_edit_row)
        self.btn_remove_row = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_remove_row.sizePolicy().hasHeightForWidth())
        self.btn_remove_row.setSizePolicy(sizePolicy)
        self.btn_remove_row.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_remove_row.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_remove_row.setFont(font)
        self.btn_remove_row.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./images/remove_row.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove_row.setIcon(icon5)
        self.btn_remove_row.setIconSize(QtCore.QSize(36, 36))
        self.btn_remove_row.setFlat(True)
        self.btn_remove_row.setObjectName("btn_remove_row")
        self.layout_row_btns.addWidget(self.btn_remove_row)
        self.horizontalLayout.addLayout(self.layout_row_btns)
        spacerItem1 = QtWidgets.QSpacerItem(
            25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.layout_serach = QtWidgets.QHBoxLayout()
        self.layout_serach.setSpacing(10)
        self.layout_serach.setObjectName("layout_serach")
        self.dropdown = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dropdown.sizePolicy().hasHeightForWidth())
        self.dropdown.setSizePolicy(sizePolicy)
        self.dropdown.setMinimumSize(QtCore.QSize(150, 25))
        self.dropdown.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dropdown.setFont(font)
        self.dropdown.setCurrentText("")
        self.dropdown.setFrame(False)
        self.dropdown.setObjectName("dropdown")
        self.layout_serach.addWidget(self.dropdown)
        self.btn_search_item = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_search_item.sizePolicy().hasHeightForWidth())
        self.btn_search_item.setSizePolicy(sizePolicy)
        self.btn_search_item.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_search_item.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search_item.setFont(font)
        self.btn_search_item.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./images/search.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search_item.setIcon(icon6)
        self.btn_search_item.setIconSize(QtCore.QSize(32, 32))
        self.btn_search_item.setFlat(True)
        self.btn_search_item.setObjectName("btn_search_item")
        self.layout_serach.addWidget(self.btn_search_item)
        self.horizontalLayout.addLayout(self.layout_serach)
        spacerItem2 = QtWidgets.QSpacerItem(
            25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fontComboBox = QtWidgets.QFontComboBox(self.frame)
        self.fontComboBox.setMinimumSize(QtCore.QSize(120, 0))
        self.fontComboBox.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Roboto")
        self.fontComboBox.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_3.addWidget(self.fontComboBox)
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Roboto")
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(20)
        self.spinBox.setProperty("value", 12)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(
            270, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btn_view_whole_project = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_view_whole_project.sizePolicy().hasHeightForWidth())
        self.btn_view_whole_project.setSizePolicy(sizePolicy)
        self.btn_view_whole_project.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_view_whole_project.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_view_whole_project.setFont(font)
        self.btn_view_whole_project.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./images/view_all.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_view_whole_project.setIcon(icon5)
        self.btn_view_whole_project.setIconSize(QtCore.QSize(36, 36))
        self.btn_view_whole_project.setFlat(True)
        self.btn_view_whole_project.setObjectName("btn_view_whole_project")
        self.horizontalLayout.addWidget(self.btn_view_whole_project)
        spacerItem4 = QtWidgets.QSpacerItem(
            25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 6, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(
            741, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.total_cost_label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.total_cost_label.sizePolicy().hasHeightForWidth())
        self.total_cost_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.total_cost_label.setFont(font)
        self.total_cost_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.total_cost_label.setObjectName("total_cost_label")
        self.horizontalLayout_2.addWidget(self.total_cost_label)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./images/new_file.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Project.setIcon(icon7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.actionNew_Project.setFont(font)
        self.actionNew_Project.setShortcutContext(
            QtCore.Qt.ApplicationShortcut)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionLoad_Project = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./images/open_file.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_Project.setIcon(icon8)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionLoad_Project.setFont(font)
        self.actionLoad_Project.setShortcutContext(
            QtCore.Qt.ApplicationShortcut)
        self.actionLoad_Project.setObjectName("actionLoad_Project")
        self.actionSave_Project = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./images/save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Project.setIcon(icon9)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionSave_Project.setFont(font)
        self.actionSave_Project.setShortcutContext(
            QtCore.Qt.ApplicationShortcut)
        self.actionSave_Project.setObjectName("actionSave_Project")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./images/save_as.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionSave_As.setFont(font)
        self.actionSave_As.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSave_As.setObjectName("actionSave_As")
        self.print_file = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./images/print.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_file.setIcon(icon11)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.print_file.setFont(font)
        self.print_file.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.print_file.setObjectName("print_file")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("./images/quit.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon12)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionQuit.setFont(font)
        self.actionQuit.setObjectName("actionQuit")
        self.menu_undo = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("./images/print.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_undo.setIcon(icon14)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_undo.setFont(font)
        self.menu_undo.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.menu_undo.setObjectName("menu_undo")
        self.menu_setting = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("./images/print.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_setting.setIcon(icon15)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menu_setting.setFont(font)
        self.menu_setting.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.menu_setting.setObjectName("menu_setting")
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionLoad_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        # self.menuFile.addAction(self.menu_setting)
        self.menuFile.addAction(self.menu_undo)
        self.menuFile.addAction(self.print_file)
        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionQuit)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        self.dropdown.setCurrentIndex(-1)
        self.menu_clickables = [self.actionSave_As, self.actionSave_Project, self.btn_add_row, self.btn_edit_row,
                                self.btn_add_tab, self.btn_remove_tab, self.btn_remove_row, self.menu_undo, self.btn_search_item, self.fontComboBox, self.spinBox, self.print_file, self.btn_view_whole_project]
        for i in self.menu_clickables:
            i.setEnabled(False)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SDDL DB"))
        self.label.setText(_translate(
            "MainWindow", "-:-"))
        self.total_cost_label.setText(_translate("MainWindow", "0"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionNew_Project.setStatusTip(
            _translate("MainWindow", "Creates new project"))
        self.actionNew_Project.setShortcut(
            _translate("MainWindow", "Ctrl+Alt+N"))
        self.actionLoad_Project.setText(
            _translate("MainWindow", "Load Project"))
        self.actionLoad_Project.setStatusTip(
            _translate("MainWindow", "Loads save project"))
        self.actionLoad_Project.setShortcut(
            _translate("MainWindow", "Ctrl+Alt+L"))
        self.actionSave_Project.setText(
            _translate("MainWindow", "Save"))
        self.actionSave_Project.setStatusTip(
            _translate("MainWindow", "Save file"))
        self.actionSave_Project.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setStatusTip(
            _translate("MainWindow", "Save file as new"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Alt+S"))
        self.print_file.setText(_translate("MainWindow", "Print"))
        self.print_file.setStatusTip(
            _translate("MainWindow", "Print current table"))
        self.print_file.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(
            _translate("MainWindow", "Closes the app"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Alt+Q"))
        self.menu_undo.setText(_translate("MainWindow", "Undo"))
        self.menu_undo.setStatusTip(
            _translate("MainWindow", "Undo Previous action"))
        self.menu_undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.menu_setting.setText(_translate("MainWindow", "Settings"))
        self.menu_setting.setStatusTip(
            _translate("MainWindow", "Open Settings"))
        self.menu_setting.setShortcut(_translate("MainWindow", "Ctrl+P"))
