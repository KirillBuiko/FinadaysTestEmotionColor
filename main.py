import sys
import os
import time
from PyQt5 import QtGui, QtWidgets, QtCore


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle('Breeze')
    pic = QtGui.QPixmap('./res/splash.jpg')
    splash = QtWidgets.QSplashScreen(pic)
    splash.show()
    import StartHelpWindow as form
    app.processEvents()
    window = form.Form()  # Создаём объект класса ExampleApp
    window.show() # Показываем окно
    splash.finish(window)
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
