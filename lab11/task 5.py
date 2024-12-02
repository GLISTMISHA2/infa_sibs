'''Реализовать для 2 задания программу с графическим интерфейсом. Дизайн за вами.'''

import PySimpleGUI as sg
sg.theme('Dark Blue 3')
s = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
    'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
    'Y': 4, 'Z': 10
}

layout = [
    [sg.Image(filename="kot.png", subsample=3)],
    [sg.Text("Введите слово:")],
    [sg.InputText(key='-WORD-')],
    [sg.Button("Рассчитать очки", key='-CALCULATE-')],
    [sg.Text("", key='-RESULT-', size=(20, 1), justification='center')]
]

window = sg.Window("Эрудит", layout, element_justification='center', size=(500, 350))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-CALCULATE-':
        word = values['-WORD-']
        points = 0
        for char in word:
            if char.upper() in s:
                points += s[char.upper()]
        window['-RESULT-'].update(f"Очки: {points}")

window.close()
