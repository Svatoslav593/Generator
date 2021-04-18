#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QVBoxLayout
from random import randint
#создание элементов интерфейса
ads = QApplication([])
czx = QWidget()
czx.show()
sjd = QLabel('Нажми, чтобы узнать победителя')
pty = QLabel('?')
ret = QPushButton('Сгенерировать')
line = QVBoxLayout()
line.addWidget(sjd, alignment = Qt.AlignCenter)
line.addWidget(pty, alignment = Qt.AlignCenter)
line.addWidget(ret, alignment = Qt.AlignCenter)
czx.setLayout(line)
def winner():
    nbv = randint(0,99)
    pty.setText(str(nbv))
    sjd.setText("Победитель:")
ret.clicked.connect(winner)
#привязка элементов к вертикальной линии

#обработка событий
#запуск приложения


ads.exec_()