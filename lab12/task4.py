import PySimpleGUI as sg

# Настройки темы и макета
sg.theme("Reddit")
layout = [
    [sg.Text(" ")],
    [sg.Text("Число:", auto_size_text=True, justification="left", font="22px"), sg.InputText(size=10, font="20px")],
    [sg.Button("Перевод", key="-function-", size=25, font="22px")],
    [sg.Text("Прямой:", key="-text1-", justification="center", font="25px")],
    [sg.Text("Обратный:", key="-text2-", justification="center", font="25px")],
    [sg.Text("Дополнительный:", key="-text3-", justification="center", font="25px")]
]

# Создание окна
window = sg.Window("Общитатель кода", layout, element_justification="left", size=(325, 260))

while True:
    event, values = window.read()
    try:
        if event == sg.WIN_CLOSED:
            break
        elif event == "-function-":
            digit = int(values[0])
            if digit > 127 or digit < -128:
                window["-text1-"].update("                 Ошибка")
                window["-text2-"].update("")
                window["-text3-"].update("")
            else:
                if digit >= 0:
                    first = bin(digit)[2:].zfill(8)
                else:
                    first = bin(digit & 0xFF)[2:].zfill(8)

                second = ""
                for i in first:
                    if i == "0":
                        second += "1"
                    else:
                        second += "0"

                thirt = bin(int(second, 2) + 1)[2:].zfill(8)

                window["-text1-"].update(f"Прямой: {first}")
                window["-text2-"].update(f"Обратный: {second}")
                window["-text3-"].update(f"Дополнительный: {thirt}")
    except ValueError:
        window["-text1-"].update("                 Ошибка")
        window["-text2-"].update("")
        window["-text3-"].update("")

window.close()
