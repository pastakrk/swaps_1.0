from PyQt4 import QtGui, QtCore

class TableModel(QtGui.QStandardItemModel):
    _sort_order = QtCore.Qt.AscendingOrder

    def sortOrder(self):
        return self._sort_order

    def sort(self, column, order):
        if column == 0:
            self._sort_order = order
            QtGui.QStandardItemModel.sort(self, column, order)

class Window(QtGui.QWidget):
    def __init__(self, rows, columns):
        QtGui.QWidget.__init__(self)
        self.table = QtGui.QTableView(self)
        model = TableModel(rows, columns, self.table)
        for row in range(rows):
            for column in range(columns):
                item = QtGui.QStandardItem('(%d, %d)' % (row, column))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                model.setItem(row, column, item)
        self.table.setModel(model)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().sortIndicatorChanged.connect(
            self.handleSortIndicatorChanged)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)

    def handleSortIndicatorChanged(self, index, order):
        if index != 0:
            self.table.horizontalHeader().setSortIndicator(
                0, self.table.model().sortOrder())

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window(5, 5)
    window.show()
    window.setGeometry(600, 300, 600, 250)
    sys.exit(app.exec_())