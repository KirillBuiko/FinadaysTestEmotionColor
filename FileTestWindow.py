import sys  # sys нужен для передачи argv в QApplication
import os
import time
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
        self.dropFilePic.setVisible(False)
        self.dropFilePic.setGeometry(0, 0, self.width(), self.height())
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
                path = e.mimeData().urls()[0].path()
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
        self.progressBar.setMaximum(100)
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
        self.animationProgress = QtCore.QPropertyAnimation(self.progressBar, b'value')
        self.animationProgress.setDuration(1000)
        self.animationProgress.setStartValue(0)
        self.animationProgress.setEndValue(100)
        self.animationProgress.start()
        self.animationProgress.finished.connect(self.progressFinished)



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle('Breeze')
    app.processEvents()
    window = Form()  # Создаём объект класса ExampleApp
    window.exec_()
    app.exec_()  # и запускаем приложение
    

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
