import PySimpleGUI as sg
import random as r

# Инициализация графического интерфейса
c_image = [[sg.Image("bio.png")]]
c_input = [
    [sg.Text("Введите количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
    [sg.Text("На сколько делиться (k):", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="kol")],
    [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
    [sg.Button("Рассчитать", font="Arial 20")]
]

layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бактерий", layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Рассчитать":
        try:
            count = int(value["count"])  # Количество секунд для расчета
            kol = int(value["kol"])      # На сколько делиться (k)

            micro = 1  # Начальное количество бактерий

            for _ in range(count):
                b = r.randint(0, 4)  # Рандомное число b в диапазоне от 0 до 4
                micro = kol * micro + b

            window["res"].update(micro)
        except ValueError:
            sg.popup_error("Пожалуйста, введите корректные числовые значения.")

window.close()
