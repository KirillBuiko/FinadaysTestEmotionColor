import sys  # sys нужен для передачи argv в QApplication
import os
import time
import math
import design.TextTestWindowDesign as design
import FileTestWindow as filetestform
from PyQt5 import QtGui, QtWidgets, QtCore


class Form(design.Ui_Form, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.res1 = 0
        self.res2 = 0
        self.text1 = ''
        self.text2 = ''
        self.setupUi(self)
        pic = QtGui.QImage('./res/text.png')
        self.setFixedSize(pic.width() , pic.height())
        self.setWindowIcon(QtGui.QIcon('./res/icon.ico'))
        self.pushButton.clicked.connect(self.pushButton_click)
        self.uploadFileButton.clicked.connect(self.uploadFileButton_click)
        self.errorLabel.setVisible(False)

    def uploadFileButton_click(self):
        self.changeForm(filetestform.Form)

    def changeForm(self, form):
        self.window = form()
        self.window.model = self.model
        self.window.ts = self.ts
        self.window.setWindowOpacity(0)
        self.animationFile = QtCore.QPropertyAnimation(self.window, b'windowOpacity')
        self.animationFile.setDuration(500)
        self.animationFile.setStartValue(0)
        self.animationFile.setEndValue(1)
        self.animationFile.start()
        self.window.exec_()

    def pushButton_click(self):
        res = self.analize()
        if res != '':
            self.errorLabel.setVisible(True)
            self.errorLabel.setText(res)
        else:
            self.errorLabel.setVisible(False)
            self.answerText.setPlainText('')
            if self.res2 != 0 and self.checkBox.isChecked() == True:
                if self.res2 > self.res1:
                    self.answerText.appendPlainText('Сообщение позитивное с меньшей на ' + str((self.res2-self.res1)*100) + ' вероятностью, чем прошлое.')
                else:
                    self.answerText.appendPlainText('Сообщение позитивное с большей на ' + str((self.res1-self.res2)*100) + '% вероятностью, чем прошлое.')
            if self.res1 > 0.8:
                self.answerText.appendPlainText('Сообщение позитивное с большой вероятностью: ' + str(self.res1*100) + '%. Пользователю стоит предложить оценить приложение.')
            elif self.res1 > 0.5:
                self.answerText.appendPlainText('Сообщение позитивное со средней вероятностью: ' + str(self.res1*100) + '%. Сообщение может быть нейтральнымю. Пользователю можно предложить оценить приложение.')
            elif self.res1 > 0.3:
                self.answerText.appendPlainText('Сообщение негативное со средней вероятностью: ' + str(round(1-self.res1, 3)*100) + '%. Сообщение может быть нейтральным, но можно обратить внимание специалистов.')
            else:
                self.answerText.appendPlainText('Сообщение негативное с большой вероятностью: ' + str(round(1-self.res1, 3)*100) + '%. Стоит обратить внимание специалистов.')
            self.answerText.appendPlainText('Вероятности эмоционального окраса этого сообщения [Позитивное/Негативное]: [' + str(self.res1) + '/' + str(round(1-self.res1, 3)) + ']')
                    
    def analize(self) -> str:
        string = self.messageText.toPlainText()
        if string.strip().__eq__(''):
            return 'Введите текст в поле ниже'
        if string.__eq__(self.text1):
            return 'Сообщение не отличается от предыдущего'
        if self.res1 != 0 :
            self.res2 = self.res1
            self.text2 = self.text1
        self.text1 = string
        self.res1 = round(self.model.predict_proba(string)[0][1],3)
        return ''



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setStyle('Breeze')
    app.processEvents()
    window = Form()  # Создаём объект класса ExampleApp
    window.show()
    app.exec_()  # и запускаем приложение
    

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
