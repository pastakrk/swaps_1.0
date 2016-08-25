import sys
import os
import csv
import numpy as np
import pandas as pd
from PyQt4 import QtCore, QtGui

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

class view(object):
    def setupUi(self, Swaps_creator):
        Swaps_creator.setObjectName(_fromUtf8("Swaps_creator"))
        Swaps_creator.resize(500, 500)
        self.tabWidget = QtGui.QTabWidget(Swaps_creator)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.otworz = QtGui.QPushButton(self.tab)
        self.otworz.setGeometry(QtCore.QRect(0, 0, 150, 50))
        self.otworz.setObjectName(_fromUtf8("otworz"))

        self.otworz.clicked.connect(self.open_file)

        self.zapisz = QtGui.QPushButton(self.tab)
        self.zapisz.setGeometry(QtCore.QRect(150, 0, 150, 50))
        self.zapisz.setObjectName(_fromUtf8("zapisz"))

        self.zapisz.clicked.connect(self.save_file)

        self.df1 = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
        self.tabela_rates = QtGui.QTableWidget(self.tab)
        self.tabela_rates.setGeometry(QtCore.QRect(0, 50, 500, 450))
        self.tabela_rates.setObjectName(_fromUtf8("tabela_rates"))
        self.tabela_rates.setColumnCount(len(self.df1.columns))
        self.tabela_rates.setRowCount(len(self.df1.index))

        self.col = range(len(self.df1.columns))
        self.row = range(len(self.df1.index))

        for i in self.col:
            self.tabela_rates.setHorizontalHeaderItem(i, QtGui.QTableWidgetItem(self.df1.columns.values[i]))
            for j in self.row:
                item = QtGui.QTableWidgetItem(str(self.df1.iloc[j,i]))
                self.tabela_rates.setItem(j, i, item)

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.otworz2 = QtGui.QPushButton(self.tab_2)
        self.otworz2.setGeometry(QtCore.QRect(0, 0, 150, 50))
        self.otworz2.setObjectName(_fromUtf8("otworz"))

        self.otworz2.clicked.connect(self.open_file)

        self.zapisz2 = QtGui.QPushButton(self.tab_2)
        self.zapisz2.setGeometry(QtCore.QRect(150, 0, 150, 50))
        self.zapisz2.setObjectName(_fromUtf8("zapisz"))

        self.zapisz2.clicked.connect(self.save_file)

        self.tabela_rates = QtGui.QTableWidget(self.tab_2)
        self.tabela_rates.setGeometry(QtCore.QRect(0, 50, 500, 450))
        self.tabela_rates.setObjectName(_fromUtf8("tabela_rates"))
        self.tabela_rates.setColumnCount(len(self.df1.columns))
        self.tabela_rates.setRowCount(len(self.df1.index))

        self.retranslateUi(Swaps_creator)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Swaps_creator)

    def retranslateUi(self, Swaps_creator):
        Swaps_creator.setWindowTitle(_translate("Swaps_creator", "Swaps_creator", None))
        self.otworz.setText(_translate("Swaps_creator", "Otwórz", None))
        self.zapisz.setText(_translate("Swaps_creator", "Zapisz", None))
        self.otworz2.setText(_translate("Swaps_creator", "Otwórz", None))
        self.zapisz2.setText(_translate("Swaps_creator", "Zapisz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Swaps_creator", "tickery", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Swaps_creator", "instrumenty", None))



class model:
    def __init__(self):
        self.final_table = pd.read_csv('base_file2.csv', sep=";")
    def get_annualized_rates(self, offer):
            self.final_table['short'+'_'+offer] = self.final_table['ask'] * ((1 + self.final_table['quote_bid'] - self.final_table[offer] / 2) / 360) / (
                (1 + self.final_table['base_ask'] + self.final_table[offer] / 2) / 360)
            self.final_table['long'+'_'+offer] = self.final_table['bid'] * ((1 + self.final_table['quote_bid'] - self.final_table[offer] / 2) / 360) / (
                (1 + self.final_table['base_ask'] + self.final_table[offer] / 2) / 360)
            return self.final_table



class controller
    def __init__(self):

    def open_file(self):
        path = QtGui.QFileDialog.getOpenFileName(None, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')
        print(path)
        if path[0] != '':
            self.my_file = pd.read_csv(path)

            self.col = range(len(self.my_file.columns))
            self.row = range(len(self.my_file.index))

            for i in self.col:
                self.tabela_rates.setHorizontalHeaderItem(i, QtGui.QTableWidgetItem(self.my_file.columns.values[i]))
                for j in self.row:
                    item = QtGui.QTableWidgetItem(str(self.my_file.iloc[j, i]))
                    self.tabela_rates.setItem(j, i, item)

    def save_file(self):
        path = QtGui.QFileDialog.getSaveFileName(None, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')

        if path[0] != '':
            with open(path, 'w') as stream:
                writer = csv.writer(stream, dialect='excel')

                for i in self.row:
                    new_file = []
                    for j in self.col:
                        item = self.tabela_rates.item(i, j)
                        if item is not None:
                            new_file.append(item.text())
                        else:
                            new_file.append('')
                    writer.writerow(new_file)


    # def get_annualized_rates(self, side, offer):
    #     if side == 'bid':
    #         rates_table = get_tickers('markup_list.csv', 'ticker', 1)
    #         rates_table['bid_rate'] = get_data('markup_list.csv', 'basic')
    #     else:
    #         rates_table = get_tickers('markup_list.csv', 'ticker', 1)
    #         rates_table['ask_rate'] = get_data('markup_list.csv', 'basic')
    #     return rates_table

    # def get_data(self, f, c):
    #         ticker_list = pd.read_csv(f)
    #         x = ticker_list[c].tolist()
    #         return x
    #
    # def get_tickers(self, f, c, t):
    #     if t == 0:
    #         bid = con.ref(get_data(f, c), ['BID'])
    #         ask = con.ref(get_data(f, c), ['ASK'])
    #         base = con.ref(get_data(f, c), ['BASE_CRNCY'])
    #         quote = con.ref(get_data(f, c), ['CRNCY'])
    #         table1 = pd.merge(bid, ask, how='left', on=['ticker'])
    #         table2 = pd.merge(table1, base, how='left', on=['ticker'])
    #         final = pd.merge(table2, quote, how='left', on=['ticker'])
    #         final.drop(['field_x', 'field_y'], axis=1, inplace=True)
    #         final.drop_duplicates(['ticker'], keep='first', inplace=True)
    #         final.columns = ['ticker', 'bid', 'ask', 'base_crncy', 'quote_crncy']
    #     else:
    #         px_last = con.ref(get_data(f, c), ['PX_LAST'])
    #         base = con.ref(get_data(f, c), ['BASE_CRNCY'])
    #         quote = con.ref(get_data(f, c), ['CRNCY'])
    #         table1 = pd.merge(px_last, base, how='left', on=['ticker'])
    #         final = pd.merge(table1, quote, how='left', on=['ticker'])
    #         final.drop(['field_x', 'field_y', 'value_y', 'field'], axis=1, inplace=True)
    #         final['quote_crncy'] = final['value']
    #         final.columns = ['ticker', 'rates_px_last', 'base_crncy', 'quote_crncy']
    #     return final
    #
    def get_annualized_rates(self, side, offer):
        if side == 'bid':
            rates_table = get_tickers('markup_list.csv', 'ticker', 1)
            rates_table['bid_rate'] = get_data('markup_list.csv', 'basic')
        else:
            rates_table = get_tickers('markup_list.csv', 'ticker', 1)
            rates_table['ask_rate'] = get_data('markup_list.csv', 'basic')
        return rates_table


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Swaps_creator = QtGui.QWidget()
    ui = view()
    ui.setupUi(Swaps_creator)
    # r1 = ui.get_annualized_rates('bid', 'basic')
    # r2 = ui.get_annualized_rates('bid', 'standard')
    # print(range(len(ui.df1.columns)))
    # print(range(len(ui.df1.index)))
    # print(type(range(len(ui.df1.columns))))
    # print(ui.df1.iloc[0,0])
    # print(type(ui.tabela_rates))
    # print(ui.df1.columns.values[1])
    Swaps_creator.show()
    sys.exit(app.exec_())