'''Напишите программу "Рандом". В программе должно быть три поля. Два для ввода границ рандома.
Третье для вывода псевдослучайного числа. И одна кнопка "Сгенерировать". А также графический
интерфейс должен включать один рисунок. Выберите тему оформления на ваш вкус. По желанию
можете поэкспериментировать с шрифтами и размерами элементом.'''

import PySimpleGUI as sg
import random as r

sg.theme('Dark Blue 3')

layout = [
    [sg.Text("Генератор случайных чисел", justification="center")],
    [sg.Image(filename="p.png", subsample=1)],
    [sg.Text("Пределы генерации", expand_x=True, auto_size_text=True, justification="center")],
    [sg.Text("С  ",), sg.InputText(size=16, key='-START-')],
    [sg.Text("По",), sg.InputText(size=16, key='-END-')],
    [sg.Button("Сгенерировать", key="-GENERATE-", size=(13, 1))],
    [sg.Text("", key="-RESULT-", justification="center")]
]

window = sg.Window("Рандомчик", layout, element_justification="center", size=(450, 530))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-GENERATE-":
        try:
            start_limit = int(values['-START-'])
            end_limit = int(values['-END-'])
            if start_limit > end_limit:
                window["-RESULT-"].update("Неправильные пределы")
            else:
                r_num = r.randint(start_limit, end_limit)
                window["-RESULT-"].update(r_num)
        except ValueError:
            window["-RESULT-"].update("Ошибка")
window.close()
