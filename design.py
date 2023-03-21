# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1072, 805)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.page.setFont(font)
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.page)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_7.addWidget(self.plainTextEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.loadFileBtnDocs = QtWidgets.QPushButton(self.page)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/setText.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadFileBtnDocs.setIcon(icon)
        self.loadFileBtnDocs.setObjectName("loadFileBtnDocs")
        self.horizontalLayout_2.addWidget(self.loadFileBtnDocs)
        self.ClearBtnDocs = QtWidgets.QPushButton(self.page)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearBtnDocs.setIcon(icon1)
        self.ClearBtnDocs.setObjectName("ClearBtnDocs")
        self.horizontalLayout_2.addWidget(self.ClearBtnDocs)
        self.playAudioBtnDocs = QtWidgets.QPushButton(self.page)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playAudioBtnDocs.setIcon(icon2)
        self.playAudioBtnDocs.setObjectName("playAudioBtnDocs")
        self.horizontalLayout_2.addWidget(self.playAudioBtnDocs)
        self.stopAudioBtnDocs = QtWidgets.QPushButton(self.page)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopAudioBtnDocs.setIcon(icon3)
        self.stopAudioBtnDocs.setObjectName("stopAudioBtnDocs")
        self.horizontalLayout_2.addWidget(self.stopAudioBtnDocs)
        self.saveAudioBtnDocs = QtWidgets.QPushButton(self.page)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAudioBtnDocs.setIcon(icon4)
        self.saveAudioBtnDocs.setObjectName("saveAudioBtnDocs")
        self.horizontalLayout_2.addWidget(self.saveAudioBtnDocs)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.comboBox.setFont(font)
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setIconSize(QtCore.QSize(30, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Taudio"))
        self.loadFileBtnDocs.setText(_translate("MainWindow", "Загрузить текст"))
        self.ClearBtnDocs.setText(_translate("MainWindow", "Очистить"))
        self.playAudioBtnDocs.setText(_translate("MainWindow", "Проиграть аудио"))
        self.stopAudioBtnDocs.setText(_translate("MainWindow", "Остановить аудио"))
        self.saveAudioBtnDocs.setText(_translate("MainWindow", "Сохранить аудио"))
        self.label_2.setText(_translate("MainWindow", "Загрузка...."))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Формат"))
        self.comboBox.setCurrentText(_translate("MainWindow", "WORD/PFD/Написать"))
        self.comboBox.setItemText(0, _translate("MainWindow", "WORD/PFD/Написать"))
        self.comboBox.setItemText(1, _translate("MainWindow", "URL"))
