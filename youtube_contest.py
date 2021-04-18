#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout, QRadioButton,QMessageBox
#создание приложения и главного окна
ads = QApplication([])
czx = QWidget()
#создание виджетов главного окна
fyt = QLabel("В каком году канал получил Золотую кнопку")
dsa = QRadioButton("2005")
dsn = QRadioButton("2015")
dst = QRadioButton("2010")
dta = QRadioButton("2020")
#расположение виджетов по лэйаутам
wer = QHBoxLayout()
rte = QHBoxLayout()
yto = QHBoxLayout()
wer.addWidget(fyt,alignment = Qt.AlignCenter)
rte.addWidget(dsa,alignment = Qt.AlignCenter)
yto.addWidget(dsn,alignment = Qt.AlignCenter)
rte.addWidget(dst,alignment = Qt.AlignCenter)
yto.addWidget(dta,alignment = Qt.AlignCenter)
tre = QVBoxLayout()
tre.addLayout(wer)
tre.addLayout(rte)
tre.addLayout(yto)
czx.setLayout(tre)
#обработка нажатий на переключатели
def lose():
    a = QMessageBox()
    a.setText("Нет,в 2015 году.Вы выиграли фирменный плакат.")
    a.exec_()
def win():
    b = QMessageBox()
    b.setText("Верно! Вы выиграли гироскутер.")
    b.exec_()
dsa.clicked.connect(lose)
dsn.clicked.connect(win)
dst.clicked.connect(lose)
dta.clicked.connect(lose)
#отображение окна приложения 
czx.show()
ads.exec_()
