'''На старых мобильных телефонах текстовые сообщения набирались при помощи цифровых кнопок.
При этом одна кнопка ассоциируется сразу с несколькими буквами, а выбор зависел от количества
нажатий на кнопку.
'''
s = {
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999',
    ' ': '0'
}
message = input("Введите сообщение: ")
r = ""
for char in message.lower():
    if char in s:
        r += s[char]
print("Последовательность кнопок:", r)