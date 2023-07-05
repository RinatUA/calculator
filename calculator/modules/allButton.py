from PyQt5.QtWidgets import (
    QPushButton
)
from modules.allLayouts import list_HLayout, main_VLayout
from modules.lists import *
#
for count in range(10):
    list_number_button.append(QPushButton(str(count)))
#
for symbol in list_name_symbol:
    list_symbol_button.append(QPushButton(symbol))
#
def sort_button():
    #
    list_sort_button = list()
    index = 7
    #
    for el in list_symbol_button:
        if len(list_sort_button) < 4:
            list_sort_button.append(el)
    list_buttons.append(list_sort_button)
    list_sort_button = list()
    #
    for el in range(4,7):
    #
        for num in range(3):
            #
            list_sort_button.append(list_number_button[index])
            index += 1
        #
        list_sort_button.append(list_symbol_button[el])
    #
        list_buttons.append(list_sort_button)
    #
        list_sort_button = list()
        index -= 6
#
def show_buttons():
    #
    for el in list_buttons:
        #
        index = list_buttons.index(el)
        #
        for button in el:
            list_HLayout[index].addWidget(button)
    # 
    list_HLayout[-1].addWidget(list_number_button[0])
    list_HLayout[-1].addWidget(list_symbol_button[-1])
    list_HLayout[-1].addWidget(list_symbol_button[-2])
    #
    for count in list_HLayout:
        main_VLayout.addLayout(count)


