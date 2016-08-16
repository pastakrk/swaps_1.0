# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
try:
    from PyQt4.QtCore import QAbstractTableModel, Qt, QVariant, QModelIndex
    from PyQt4.QtGui import (
        QApplication, QDialog, QVBoxLayout, QTableView, QWidget)
except ImportError:
    from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex
    from PySide.QtGui import (
        QApplication, QDialog, QVBoxLayout, QTableView, QWidget)
    QVariant = lambda value=None: value

import numpy as np
import pandas as pd
from PyQt4 import QtCore, QtGui
#from pandas.sandbox.qtpandas import DataFrameModel, DataFrameWidget
import sys


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Swaps_creator(object):

    def setupUi(self, Swaps_creator):
        Swaps_creator.setObjectName(_fromUtf8("Swaps_creator"))
        Swaps_creator.resize(500, 500)
        self.tabWidget = QtGui.QTabWidget(Swaps_creator)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))

        self.otworz = QtGui.QPushButton(self.tab)
        self.otworz.setGeometry(QtCore.QRect(0, 0, 150, 50))
        self.otworz.setObjectName(_fromUtf8("otworz"))

        self.zapisz = QtGui.QPushButton(self.tab)
        self.zapisz.setGeometry(QtCore.QRect(150, 0, 150, 50))
        self.zapisz.setObjectName(_fromUtf8("zapisz"))

        self.df1 = pd.DataFrame(np.random.randn(100, 3), columns=['foo', 'bar', 'baz'])
        self.tabela_rates = QtGui.QTableWidget(self.df1)
        self.tabela_rates.setGeometry(QtCore.QRect(0, 50, 500, 450))
        self.tabela_rates.setObjectName(_fromUtf8("tabela_rates"))
        self.tabela_rates.setColumnCount(0)
        self.tabela_rates.setRowCount(0)

        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Swaps_creator)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Swaps_creator)

    def retranslateUi(self, Swaps_creator):
        Swaps_creator.setWindowTitle(_translate("Swaps_creator", "Swaps_creator", None))
        self.otworz.setText(_translate("Swaps_creator", "Otwórz", None))
        self.zapisz.setText(_translate("Swaps_creator", "Zapisz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Swaps_creator", "tickery", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Swaps_creator", "instrumenty", None))

    def get_data(self, f, c):
        ticker_list = pd.read_csv(f)
        x = ticker_list[c].tolist()
        return x

    def get_annualized_rates(self, side, offer):
        if side == 'bid':
            rates_table = self.get_data('markup_list.csv', 'ticker')
        else:
            rates_table = self.get_data('markup_list.csv', 'ticker')
        return rates_table

    def ticker_table(self):
        self.df1 = pd.DataFrame(np.random.randn(100,3), columns=['foo', 'bar', 'baz'])
        return self.df1

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Swaps_creator = QtGui.QWidget()
    ui = Ui_Swaps_creator()
    ui.setupUi(Swaps_creator)
    r1 = ui.get_annualized_rates('bid', 'basic')
    r2 = ui.get_annualized_rates('bid', 'standard')
    print(r1,r2)
    print(type(r1))
    Swaps_creator.show()
    sys.exit(app.exec_())