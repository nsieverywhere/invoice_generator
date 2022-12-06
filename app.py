# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sjpfi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main import runProcess
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GeneratePFI = QtWidgets.QPushButton(self.centralwidget)
        self.GeneratePFI.setGeometry(QtCore.QRect(410, 480, 221, 23))
        self.GeneratePFI.setObjectName("GeneratePFI")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 10, 521, 93))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_vat = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_vat.setObjectName("label_vat")
        self.gridLayout.addWidget(self.label_vat, 2, 0, 1, 1)
        self.label_chargewithvat = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_chargewithvat.setObjectName("label_chargewithvat")
        self.gridLayout.addWidget(self.label_chargewithvat, 1, 2, 1, 1)
        self.chargewithoutvat = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.chargewithoutvat.setObjectName("chargewithoutvat")
        self.gridLayout.addWidget(self.chargewithoutvat, 1, 1, 1, 1)
        self.label_date = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_date.setObjectName("label_date")
        self.gridLayout.addWidget(self.label_date, 0, 0, 1, 1)
        self.invoiceno = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.invoiceno.setObjectName("invoiceno")
        self.gridLayout.addWidget(self.invoiceno, 2, 4, 1, 1)
        self.pfi_title = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pfi_title.setObjectName("pfi_title")
        self.gridLayout.addWidget(self.pfi_title, 0, 4, 1, 1)
        self.chargewithvat = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.chargewithvat.setObjectName("chargewithvat")
        self.gridLayout.addWidget(self.chargewithvat, 1, 4, 1, 1)
        self.label_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_title.setObjectName("label_title")
        self.gridLayout.addWidget(self.label_title, 0, 2, 1, 1)
        self.date = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 0, 1, 1, 1)
        self.label_chargewithoutvat = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_chargewithoutvat.setObjectName("label_chargewithoutvat")
        self.gridLayout.addWidget(self.label_chargewithoutvat, 1, 0, 1, 1)
        self.vat = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.vat.setObjectName("vat")
        self.gridLayout.addWidget(self.vat, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 2, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(110, 110, 521, 349))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.desc1 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.desc1.setObjectName("desc1")
        self.gridLayout_2.addWidget(self.desc1, 1, 1, 1, 1)
        self.label_description = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_description.setObjectName("label_description")
        self.gridLayout_2.addWidget(self.label_description, 0, 1, 1, 1)
        self.desc2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.desc2.setObjectName("desc2")
        self.gridLayout_2.addWidget(self.desc2, 2, 1, 1, 1)
        self.desc4 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.desc4.setObjectName("desc4")
        self.gridLayout_2.addWidget(self.desc4, 4, 1, 1, 1)
        self.netvalue1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.netvalue1.setObjectName("netvalue1")
        self.gridLayout_2.addWidget(self.netvalue1, 1, 3, 1, 1)
        self.quantity1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.quantity1.setObjectName("quantity1")
        self.gridLayout_2.addWidget(self.quantity1, 1, 2, 1, 1)
        self.quantity2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.quantity2.setObjectName("quantity2")
        self.gridLayout_2.addWidget(self.quantity2, 2, 2, 1, 1)
        self.netvalue2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.netvalue2.setObjectName("netvalue2")
        self.gridLayout_2.addWidget(self.netvalue2, 2, 3, 1, 1)
        self.netvalue3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.netvalue3.setObjectName("netvalue3")
        self.gridLayout_2.addWidget(self.netvalue3, 3, 3, 1, 1)
        self.desc3 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.desc3.setObjectName("desc3")
        self.gridLayout_2.addWidget(self.desc3, 3, 1, 1, 1)
        self.quantity3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.quantity3.setObjectName("quantity3")
        self.gridLayout_2.addWidget(self.quantity3, 3, 2, 1, 1)
        self.quantity4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.quantity4.setObjectName("quantity4")
        self.gridLayout_2.addWidget(self.quantity4, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_netvalue = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_netvalue.setObjectName("label_netvalue")
        self.gridLayout_2.addWidget(self.label_netvalue, 0, 3, 1, 1)
        self.netvalue4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.netvalue4.setObjectName("netvalue4")
        self.gridLayout_2.addWidget(self.netvalue4, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 470, 231, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 490, 211, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def dothis():
            runProcess(self.vat.text(), self.date.text(),
                       self.pfi_title.text(),
                       self.chargewithvat.text(),
                       self.chargewithoutvat.text(),
                       self.desc1.toPlainText(),
                       self.netvalue1.text(),
                       self.invoiceno.text(),
                       self.desc2.toPlainText(),
                       self.desc3.toPlainText(),
                       self.desc4.toPlainText(),
                       self.netvalue2.text(),
                       self.netvalue3.text(),
                       self.netvalue4.text(),
                       self.quantity1.text(),
                       self.quantity2.text(),
                       self.quantity3.text(),
                       self.quantity4.text()


                       )

        self.GeneratePFI.clicked.connect(dothis)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GeneratePFI.setText(_translate("MainWindow", "Generate Document"))
        self.label_vat.setText(_translate("MainWindow", "VAT:"))
        self.label_chargewithvat.setText(_translate("MainWindow", "Charge with VAT:"))
        self.label_date.setText(_translate("MainWindow", "Date:"))
        self.label_title.setText(_translate("MainWindow", "PFI Title:"))
        self.label_chargewithoutvat.setText(_translate("MainWindow", "Charge without Vat:"))
        self.label.setText(_translate("MainWindow", "Invoice No:"))
        self.label_description.setText(_translate("MainWindow", "Description"))
        self.label_2.setText(_translate("MainWindow", "Quantity"))
        self.label_netvalue.setText(_translate("MainWindow", "Net Value"))
        self.label_3.setText(_translate("MainWindow", "1"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.label_5.setText(_translate("MainWindow", "3"))
        self.label_6.setText(_translate("MainWindow", "4"))
        self.label_7.setText(_translate("MainWindow", "Note: To generate invoice fill the invoice No"))
        self.label_8.setText(_translate("MainWindow", "To generate PFI omit the Invoice No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

