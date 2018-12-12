import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(7, 31, 0, 0)
        self.setWindowTitle('Предсказатель наследования')
        self.setFixedSize(600, 500)
        self.parent1 = QLineEdit(self)
        self.parent1.setGeometry(165, 50, 110, 30)
        self.parent1.setFont(QFont("Times", 18, QFont.Bold))
        self.parent1.setText("AABBCC")
        self.parent2 = QLineEdit(self)
        self.parent2.setGeometry(325, 50, 110, 30)
        self.parent2.setFont(QFont("Times", 18, QFont.Bold))
        self.parent2.setText("AABBCC")
        self.mainbutton = QPushButton(self)
        self.mainbutton.setGeometry(260, 5, 80, 40)
        self.mainbutton.setText("Прогноз")
        self.mainbutton.setFont(QFont("Times", 13, QFont.Bold))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
