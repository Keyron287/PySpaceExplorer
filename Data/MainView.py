# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Systems = QtWidgets.QListWidget(self.widget_3)
        self.Systems.setObjectName("Systems")
        self.verticalLayout_2.addWidget(self.Systems)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.Planets = QtWidgets.QListWidget(self.widget_4)
        self.Planets.setObjectName("Planets")
        self.verticalLayout_3.addWidget(self.Planets)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Space = QtWidgets.QListWidget(self.widget_2)
        self.Space.setObjectName("Space")
        self.verticalLayout.addWidget(self.Space)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.Orbit = QtWidgets.QListWidget(self.widget_2)
        self.Orbit.setObjectName("Orbit")
        self.verticalLayout.addWidget(self.Orbit)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.Landed = QtWidgets.QListWidget(self.widget_2)
        self.Landed.setObjectName("Landed")
        self.verticalLayout.addWidget(self.Landed)
        self.horizontalLayout.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.next_tick = QtWidgets.QPushButton(self.widget_5)
        self.next_tick.setObjectName("next_tick")
        self.horizontalLayout_2.addWidget(self.next_tick)
        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionGalaxy_Map = QtWidgets.QAction(MainWindow)
        self.actionGalaxy_Map.setObjectName("actionGalaxy_Map")
        self.actionSystem_View = QtWidgets.QAction(MainWindow)
        self.actionSystem_View.setObjectName("actionSystem_View")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionGalaxy_Map)
        self.menuView.addAction(self.actionSystem_View)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Galaxy"))
        self.label_2.setText(_translate("MainWindow", "System"))
        self.label_3.setText(_translate("MainWindow", "Space"))
        self.label_4.setText(_translate("MainWindow", "Orbit"))
        self.label_5.setText(_translate("MainWindow", "Land"))
        self.next_tick.setText(_translate("MainWindow", "Tick"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionGalaxy_Map.setText(_translate("MainWindow", "Galaxy Map"))
        self.actionSystem_View.setText(_translate("MainWindow", "System View"))
