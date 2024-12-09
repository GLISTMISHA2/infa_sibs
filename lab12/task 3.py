import PySimpleGUI as sg
import random as r

# Настройки темы и макета для калькулятора бактерий
sg.theme("Reddit")
c_image = [[sg.Image("bio.png")]]
c_input = [
    [sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
    [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
    [sg.Text("На сколько делиться:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="kol")],
    [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
    [sg.Button("Рассчитать", font="Arial 20")]
]

# Объединение макетов
layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

# Создание окна
window = sg.Window("Калькулятор бактерий", layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Рассчитать":
        try:
            micro = int(value["micro"])  # изначальное количество бактерий
            count = int(value["count"])  # количество секунд для расчета
            kol = int(value["kol"])      # коэффициент деления
            res = micro                  # начальное количество бактерий

            # Расчет количества бактерий на N-й секунде
            for _ in range(count):
                b = r.randint(0, 4)
                res = kol * res + b

            # Обновление результата в интерфейсе
            window["res"].update(res)
        except ValueError:
            window["res"].update("Ошибка ввода")

window.close()
