import random as r

# Открываем файл для чтения
with open("for7.txt", "r", encoding="utf8") as k:
    z = k.readlines()

# Генерация пароля
while True:
    first = r.choice(z).strip().capitalize()
    second = r.choice(z).strip().capitalize()
    
    # Проверка длины слов
    if len(first) >= 3 and len(second) >= 3:
        password = first + second
        
        # Проверка длины пароля
        if 8 <= len(password) <= 10:
            print("Сгенерированный пароль:", password)
            break
