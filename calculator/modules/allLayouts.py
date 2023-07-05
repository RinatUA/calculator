from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout
)
#
list_HLayout = []
#
main_VLayout = QVBoxLayout()

main_VLayout.setSpacing(1)
#
for number in range(5):
    list_HLayout.append(QHBoxLayout())


