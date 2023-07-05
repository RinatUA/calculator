from modules.lists import *
#
width = 56
height = 56
font_size = 28
color_text = (225,225,225)
bg_color = (178, 25, 14)
#
def button_style():
    for el in range(3, 8):
        list_symbol_button[el].setStyleSheet(
            f'''
                background-color: red;
                color: rgb{color_text};
                font-size: {font_size}px;
                max-width: {width}px;
                max-height: {height}px;
            '''
        )
    
    for el in range(0,3):
        list_symbol_button[el].setStyleSheet(
            f'''
                background-color: purple;
                color: rgb{color_text};
                font-size: {font_size}px;
                max-width: {width}px;
                max-height: {height}px;
            '''
        )
    
    for el in range(1, len(list_number_button)):
        list_number_button[el].setStyleSheet(
            f'''
                background-color: green;
                color: rgb{color_text};
                font-size: {font_size}px;
                max-width: {width}px;
                max-height: {height}px;
            '''
        )
    
    list_symbol_button[-1].setStyleSheet(
        f'''
            background-color: rgb{bg_color};
            color: rgb{color_text};
            font-size: {font_size}px;
            max-width: {width}px;
            max-height: {height}px;
        '''
        )

    list_number_button[0].setStyleSheet(
        f'''
            max-width: 115px; 
            max-height: {height}px;
            background-color: rgb{bg_color}; 
            color: rgb{color_text};
            font-size: {font_size}px;
        '''
    )

    
button_style()