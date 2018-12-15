import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, \
    QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.move(100, 100)
        self.setWindowTitle('Предсказатель')
        self.setFixedSize(500, 600)
        self.parent1 = QLineEdit(self)
        self.parent1.setFont(QFont('SansSerif', 15))
        self.parent1.setGeometry(120, 100, 90, 30)
        self.parent2 = QLineEdit(self)
        self.parent2.setFont(QFont('SansSerif', 15))
        self.parent2.setGeometry(310, 100, 90, 30)
        self.predict = QPushButton(self)
        self.predict.setGeometry(220, 45, 80, 30)
        self.predict.setText("Прогноз")
        self.predict.clicked.connect(self.prediction)
        self.error = QLabel(self)
        self.error.setText("Введены неверные данные. Ошибка.")
        self.error.setFont(QFont('SansSerif', 22))
        self.error.setStyleSheet("color: red;")
        self.error.move(5, 550)
        self.error.hide()
        self.percents = QLabel(self)
        self.percents.hide()
        self.percents.setGeometry(10, 260, 500, 50)
        self.percents.setFont(QFont("SansSerif", 10))
        self.changeView = QPushButton(self)
        self.changeView.setGeometry(220, 100, 80, 30)
        self.changeView.setText("Числа")
        self.changeView.clicked.connect(self.change)
        self.changeView.hide()
        self.show()

    def change(self):
        if self.sender().text() == "Числа":
            self.percents.setText("A и B доминантные - " + str(
                self.AB) + "; A доминнатный, B рецессивный - " + str(
                self.A) + ";\nB доминантный, A рецессивный - " + str(
                self.B) + "; нет доминантных - " + str(
                self.ab) + ".")
            self.changeView.setText("Проценты")
        else:
            self.percents.setText("A и B доминантные - " + str(float(
                self.AB) / 16.0 * 100) + "%; A доминнатный, B рецессивный - " + str(
                float(
                    self.A) /
                16.0 * 100) + "%;\nB доминантный, A рецессивный - " + str(
                float(self.B) / 16.0 * 100) + "%; нет доминантных - " + str(
                float(self.ab) / 16.0 * 100) + "% случаев.")
            self.changeView.setText("Числа")

    def prediction(self):
        self.clicks = 0
        self.error.hide()
        self.A = 0
        self.B = 0
        self.AB = 0
        self.ab = 0
        if len(self.parent1.text()) != 4 and len(self.parent1.text()) != 6:
            self.error.show()
        else:
            parent1 = self.parent1.text()
            parent2 = self.parent2.text()
            self.parent1.setText("")
            self.parent2.setText("")
            if len(parent1) != len(parent2):
                self.error.show()
            elif len(parent1) == 4:
                results = [[], []]
                buttons = []
                for i in range(2):
                    for i1 in range(2, 4):
                        li = []
                        li1 = []
                        li.append([parent1[i]])
                        li.append([parent1[i1]])
                        li1.append([parent2[i]])
                        li1.append([parent2[i1]])
                        results[0].append(li)
                        results[1].append(li1)
                for i in range(4):
                    for i2 in range(4):
                        res = ''
                        for i1 in range(2):
                            res += ''.join(
                                results[0][i][i1] + results[1][i2][i1])
                        buttons.append(res)
                for i in range(4):
                    for i1 in range(4):
                        self.bu = QPushButton(self)
                        self.bu.setText(buttons[i * 4 + i1])
                        self.bu.setGeometry(130 + 60 * i1, 310 + 60 * i, 60,
                                            60)
                        self.bu.show()
                        self.bu.clicked.connect(self.click)
                for i in buttons:
                    if ('A' in i) and ('B' in i):
                        self.AB += 1
                    elif 'A' in i:
                        self.A += 1
                    elif 'B' in i:
                        self.B += 1
                    else:
                        self.ab += 1
                self.percents.setText(
                    "A и B доминантные - " + str(float(self.AB) /
                                                 16.0 *
                                                 100) +
                    "%; A доминнатный, B рецессивный - " +
                    str(float(self.A) / 16.0 * 100) +
                    "%;\nB доминантный, A рецессивный - " +
                    str(float(self.B) / 16.0 * 100) +
                    "%; нет доминантных - " + str(float(
                        self.ab) /
                                                  16.0 * 100) +
                    "% случаев.")
                self.percents.show()
                self.changeView.show()

    def click(self):
        if self.clicks % 2 == 0:
            self.parent1.setText(self.sender().text())
        else:
            self.parent2.setText(self.sender().text())
        self.clicks += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
