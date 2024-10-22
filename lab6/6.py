'''1. Добавьте в игру счетчик попыток, чтобы при каждом вводе числа вместо знака > выводился
номер попытки.
2. Подсказывайте пользователю. После каждой попытки программа должна сообщать, больше ли
загаданное число, или меньше.
3. После того, как пользователь отгадал число, спросите у него хочет ли он сыграть снова? Если
да, то загадайте новое число.'''

import random

while True:
    secret = random.randint(1, 10)
    attempts = 0
    print("Хорошо, я загадал число. Попробуй его отгадать")

    while True:
        attempts += 1
        num = int(input(f"Попытка {attempts}: "))

        if num == secret:
            print("Поздравляю! Вы угадали число за :",attempts)
            break
        elif num < secret:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

    play = input("Сыграть снова? (да нет): ")
    if play != 'да':
        break
