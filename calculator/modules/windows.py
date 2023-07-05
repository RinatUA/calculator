from PyQt5.QtWidgets import(
    QApplication,
    QWidget
)
from modules.allLayouts import main_VLayout
#
app = QApplication([])
#
win = QWidget()
#
win.setWindowTitle("Calculator")
#
win.resize(300, 400)
#
win.setLayout(main_VLayout)
win.setStyleSheet("background-color: rgb(80,80,80);")