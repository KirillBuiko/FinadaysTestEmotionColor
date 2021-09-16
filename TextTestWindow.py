import sys  # sys нужен для передачи argv в QApplication
import os
import time
import design.TextTestWindowDesign as design
import FileTestWindow as filetestform
from PyQt5 import QtGui, QtWidgets, QtCore


class Form(design.Ui_Form, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pic = QtGui.QImage('./res/text.png')
        self.setFixedSize(pic.width() , pic.height())
        self.setWindowIcon(QtGui.QIcon('./res/icon.ico'))
        self.uploadFileButton.clicked.connect(self.uploadFileButton_click)

    def uploadFileButton_click(self):
        self.changeForm(filetestform.Form)

    def changeForm(self, form):
        self.window = form()
        self.window.setWindowOpacity(0)
        self.animationFile = QtCore.QPropertyAnimation(self.window, b'windowOpacity')
        self.animationFile.setDuration(500)
        self.animationFile.setStartValue(0)
        self.animationFile.setEndValue(1)
        self.animationFile.start()
        self.window.exec_()
        

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle('Breeze')
    app.processEvents()
    window = Form()  # Создаём объект класса ExampleApp
    window.show()
    app.exec_()  # и запускаем приложение
    

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
