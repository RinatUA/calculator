from modules.lists import list_input
# from modules.labels import label

def arithmeticsOperation():
    if list_input[1] == "+":
        number = float(list_input[0]) + float(list_input[2])
    elif list_input[1] == "-":
        number = float(list_input[0]) - float(list_input[2])
    elif list_input[1] == "x":
        number = float(list_input[0]) * float(list_input[2])
    elif list_input[1] == "÷":
        try:
            number = float(list_input[0]) / float(list_input[2])
        except:
            number = "Can't divide by zero"
    elif list_input[1] == "%":
        if len(list_input) <= 2 and len(list_input) > 0:
            number = float(list_input[0]) / 100
        # elif len(list_input) == 3:
            # number = float(list_input[2]) / 100
            # list_input[2] = number
            # label.setText(number)
    return number