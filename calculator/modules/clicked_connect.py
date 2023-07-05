from numpy import index_exp
from modules.lists import list_number_button, list_symbol_button
from modules.symbol_operation import *

for el in range(0,10):
    list_number_button[el].clicked.connect(list_function[el])

list_symbol_button[6].clicked.connect(add_plus)
list_symbol_button[5].clicked.connect(add_minus)
list_symbol_button[-2].clicked.connect(add_equal)
list_symbol_button[3].clicked.connect(add_division)
list_symbol_button[4].clicked.connect(add_multiplication)
list_symbol_button[0].clicked.connect(add_AC)
list_symbol_button[1].clicked.connect(add_plusminus)
list_symbol_button[-1].clicked.connect(add_float)
list_symbol_button[2].clicked.connect(add_percent)