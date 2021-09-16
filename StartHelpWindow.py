import sys
import os
import time
import threading
import design.StartHelpWindowDesign as design
import TextTestWindow as texttestform
from PyQt5 import QtGui, QtWidgets, QtCore


class Form(design.Ui_Form, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pic = QtGui.QImage('./res/start.png')
        self.setFixedSize(pic.width() , pic.height())
        self.setWindowIcon(QtGui.QIcon('./res/icon.ico'))
        self.nextButton.clicked.connect(self.nextButton_click)

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папу")
        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

    def nextButton_click(self):
        self.changeForm(texttestform.Form)
        
    def changeForm(self, form):
        self.window = form()
        self.window.setWindowOpacity(0)
        self.window.show()
        self.animation1 = QtCore.QPropertyAnimation(self, b'windowOpacity')
        self.animation1.setDuration(500)
        self.animation1.setStartValue(1)
        self.animation1.setEndValue(0)
        self.animation2 = QtCore.QPropertyAnimation(self.window, b'windowOpacity')
        self.animation2.setDuration(500)
        self.animation2.setStartValue(0)
        self.animation2.setEndValue(1)
        self.animation1.start()
        self.animation2.start()
        self.animation1.finished.connect(self.close)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle('Breeze')
    app.processEvents()
    window = Form()  # Создаём объект класса ExampleApp
    window.show() # Показываем окно
    app.exec_()  # и запускаем приложение
    

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
