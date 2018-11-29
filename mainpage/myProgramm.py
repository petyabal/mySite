import sys
# Импортируем наш интерфейс
from InitialForm import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_InitialForm()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку                     
        self.ui.pushButton.clicked.connect(self.DomainCheck)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку                  
    def DomainCheck(self):
        pass

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
