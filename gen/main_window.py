# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(414, 275)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 41, 21))
        self.te_path = QLineEdit(self.centralwidget)
        self.te_path.setObjectName(u"te_path")
        self.te_path.setGeometry(QRect(60, 30, 261, 20))
        self.btnPath = QPushButton(self.centralwidget)
        self.btnPath.setObjectName(u"btnPath")
        self.btnPath.setGeometry(QRect(330, 30, 61, 23))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 41, 21))
        self.te_name1 = QLineEdit(self.centralwidget)
        self.te_name1.setObjectName(u"te_name1")
        self.te_name1.setGeometry(QRect(60, 70, 131, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 70, 41, 21))
        self.te_name2 = QLineEdit(self.centralwidget)
        self.te_name2.setObjectName(u"te_name2")
        self.te_name2.setGeometry(QRect(260, 70, 131, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 110, 31, 21))
        self.de_time = QDateEdit(self.centralwidget)
        self.de_time.setObjectName(u"de_time")
        self.de_time.setGeometry(QRect(60, 110, 131, 22))
        self.de_time.setReadOnly(True)
        self.btnOk = QPushButton(self.centralwidget)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setGeometry(QRect(110, 230, 191, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84:", None))
        self.btnPath.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d1: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d2: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f:", None))
        self.btnOk.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
    # retranslateUi

