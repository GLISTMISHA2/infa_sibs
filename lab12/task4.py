import PySimpleGUI as sg

def to_binary(num, bits=8):
    """Преобразует число в двоичный формат с заданным количеством бит."""
    return format(num & ((1 << bits) - 1), f'0{bits}b')

def to_direct_code(num, bits=8):
    """Преобразует число в прямой код."""
    if num < 0:
        return '1' + to_binary(-num, bits-1)
    else:
        return '0' + to_binary(num, bits-1)

def to_inverse_code(num, bits=8):
    """Преобразует число в обратный код."""
    if num < 0:
        return '1' + ''.join('1' if x == '0' else '0' for x in to_binary(-num, bits-1))
    else:
        return '0' + to_binary(num, bits-1)

def to_additional_code(num, bits=8):
    """Преобразует число в дополнительный код."""
    if num < 0:
        return to_binary(2**(bits-1) + num, bits)
    else:
        return to_binary(num, bits)

# Инициализация графического интерфейса
layout = [
    [sg.Text("Введите число от -128 до 127:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="number")],
    [sg.Text("Прямой код:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="direct")],
    [sg.Text("Обратный код:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="inverse")],
    [sg.Text("Дополнительный код:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="additional")],
    [sg.Button("Преобразовать", font="Arial 20")]
]

window = sg.Window("Преобразование чисел в коды", layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Преобразовать":
        try:
            num = int(value["number"])
            if -128 <= num <= 127:
                direct_code = to_direct_code(num)
                inverse_code = to_inverse_code(num)
                additional_code = to_additional_code(num)

                window["direct"].update(direct_code)
                window["inverse"].update(inverse_code)
                window["additional"].update(additional_code)
            else:
                sg.popup_error("Число должно быть в диапазоне от -128 до 127.")
        except ValueError:
            sg.popup_error("Пожалуйста, введите корректное целое число.")

window.close()
