import sys  # sys нужен для передачи argv в QApplication
import os
import time
import threading as th
import pandas as pd
from typing import Optional
import design.FileTestWindowDesign as design
from PyQt5 import QtGui, QtWidgets, QtCore


class Form(design.Ui_Form, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pic = QtGui.QImage('./res/file.png')
        self.setFixedSize(pic.width() , pic.height())
        self.setWindowIcon(QtGui.QIcon('./res/icon.ico'))
        self.notAttached()
        self.attachFileButton.clicked.connect(self.attachButton_click)
        self.pushButton.clicked.connect(self.pushButton_click)
        self.downloadResultButton.clicked.connect(self.downloadButton_click)
        self.dropFilePic.setVisible(False)
        self.dropFilePic.setGeometry(0, 0, pic.width() , pic.height())
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()
            name = e.mimeData().urls()[0].fileName()
            if str(name).split('.')[1].lower().__eq__('csv'):
                self.dropFilePic.setVisible(True)

    def dragLeaveEvent(self, e):
        self.dropFilePic.setVisible(False)

    def dropEvent(self, e):
        if e.mimeData().hasUrls():
            self.dropFilePic.setVisible(False)
            name = e.mimeData().urls()[0].fileName()
            if str(name).split('.')[1].lower().__eq__('csv'):
                path = e.mimeData().urls()[0].path()[1:]
                self.fileNameLabel.setPlainText(e.mimeData().urls()[0].fileName())
                self.path = path
                self.attached()

    def attached(self):
        self.notAttached()
        self.pushButton.setEnabled(True)

    def progressStart(self):
        self.notAttached()
        self.attachFileButton.setEnabled(False)
        self.setAcceptDrops(False)
        self.progressBar.setVisible(True)
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)

    def progressFinished(self):
        self.attachFileButton.setEnabled(True)
        self.setAcceptDrops(True)
        self.progressBar.setVisible(False)
        self.resultTable.setVisible(True)
        self.pushButton.setEnabled(True)
        self.downloadResultButton.setVisible(True)

    def notAttached(self):
        self.attachFileButton.setEnabled(True)
        self.progressBar.setVisible(False)
        self.resultTable.setVisible(False)
        self.pushButton.setEnabled(False)
        self.downloadResultButton.setVisible(False)

    def attachButton_click(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл для обработки",filter='CSV (*.csv)')
        if not file[0].__eq__(''):
            path = file[0].split('/')
            self.path = file[0]
            self.fileNameLabel.setPlainText(path[len(path) - 1])
            self.attached()

    def pushButton_click(self):
        self.progressStart()
        thread = th.Thread(target = self.csvWork)
        thread.start()
        #self.data.to_csv('result.csv')

    def downloadButton_click(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить результаты", 'result.csv','CSV (*.csv)')
        if not file[0].__eq__(''):
            path = file[0]
            self.data.to_csv(path)
        
    def csvWork(self):
        self.data = pd.read_csv(self.path)
        table = PandasModel(self.data)
        self.resultTable.setModel(table)
        QtCore.QMetaObject.invokeMethod(self.progressBar, "setMaximum", QtCore.Q_ARG(int, len(self.data.index)))
        self.data["positive"] = 0
        self.data["negative"] = 0
        self.data["result"] = 0
        count = 0
        self.a = 5
        for name in self.data["Sender"]:
            if (name == "CLIENT"):
                text=self.data["Message"].iloc[count]
                #translation = self.ts.google(text)
                translation = text
                positive = self.model.predict_proba(translation)[0][1]
                negative = self.model.predict_proba(translation)[0][0]
                result = self.model.predict(translation)
                self.data["positive"].iloc[count] = positive
                self.data["negative"].iloc[count] = negative
                self.data["result"].iloc[count] = 'pos' if result == 1 else 'neg'
            count += 1
            QtCore.QMetaObject.invokeMethod(self.progressBar, "setValue", QtCore.Q_ARG(int, count))
        table = PandasModel(self.data)
        self.progressFinished()
        #QtCore.QMetaObject.invokeMethod(self, "progressFinished")

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.iloc[index.row()][index.column()]))
        return QtCore.QVariant()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle('Breeze')
    app.processEvents()
    window = Form()  # Создаём объект класса ExampleApp
    window.show()
    app.exec_()  # и запускаем приложение
    

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
