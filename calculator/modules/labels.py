from ctypes import alignment

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from modules.allLayouts import main_VLayout
from modules.fonts import font1
#
label = QLabel("_")
#
label.setFont(font1)
#
main_VLayout.addWidget(label, alignment= Qt.AlignRight)

label.setStyleSheet(
        '''
            color: rgb(225, 225, 225);
        '''
    )
