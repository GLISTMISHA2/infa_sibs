import PySimpleGUI as sg
import random

# Настройки темы и макета
sg.theme("DarkBlue")
layout = [
    [sg.Text("Имя игрока:", font="Arial 20"), sg.Input(font="Arial 20", size=(20, 1), key="player_name")],
    [sg.Text("Количество раундов:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 1), key="rounds")],
    [sg.Button("Начать игру", font="Arial 20", key="start")],
    [sg.Text("", font="Arial 20", key="result", size=(60, 2))],
    [sg.Button(image_filename="nrock.png", key="rock", visible=False),
     sg.Button(image_filename="ns.png", key="scissors", visible=False),
     sg.Button(image_filename="np.png", key="paper", visible=False)],
    [sg.Text("", font="Arial 20", key="score", size=(60, 2))]
]

# Создание окна с увеличенным размером
window = sg.Window("Камень-ножницы-бумага", layout, size=(900, 700))

# Переменные для хранения результатов
player_score = 0
computer_score = 0
rounds_played = 0
total_rounds = 0
player_name = ""

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "start":
        player_name = values["player_name"]
        total_rounds = int(values["rounds"])
        window["start"].update(visible=False)
        window["rock"].update(visible=True)
        window["scissors"].update(visible=True)
        window["paper"].update(visible=True)
        window["result"].update("")
        window["score"].update("")

    if event in ["rock", "scissors", "paper"]:
        user_choice = event
        computer_choice = random.choice(["rock", "scissors", "paper"])

        if user_choice == computer_choice:
            result = "Ничья"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result = "Вы победили!"
            player_score += 1
        else:
            result = "Компьютер победил!"
            computer_score += 1

        rounds_played += 1
        window["result"].update(f"Вы выбрали: {user_choice}, Компьютер выбрал: {computer_choice}, {result}")
        window["score"].update(f"Счет: {player_name} - {player_score}, Компьютер - {computer_score}")

        if rounds_played == total_rounds:
            with open("game_results.txt", "a", encoding="utf-8") as file:
                file.write(f"Имя игрока: {player_name}, Раунды: {total_rounds}, Счет: {player_name} - {player_score}, Компьютер - {computer_score}\n")
            window["result"].update("Игра завершена. Результаты записаны в файл.")
            window["rock"].update(visible=False)
            window["scissors"].update(visible=False)
            window["paper"].update(visible=False)
            window["start"].update(visible=True)
            player_score = 0
            computer_score = 0
            rounds_played = 0

window.close()
