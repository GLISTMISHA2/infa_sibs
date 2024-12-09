# Запрашиваем у пользователя выбор действия
choice = int(input("Дешифровка - 1 / Шифрование - 2: "))

if choice == 1:
    # Дешифровка сообщения
    with open('for6.txt', 'r', encoding='utf-8') as file:
        encrypted_lines = file.readlines()

    decrypted_message = []
    for line in encrypted_lines:
        words = line.split()
        decrypted_words = [word[::-1] for word in words]
        decrypted_message.append(' '.join(decrypted_words))

    print("Расшифрованное сообщение:")
    print('\n'.join(decrypted_message))

elif choice == 2:
    # Шифрование сообщения
    message = input("Введите строку для шифрования: ")
    words = message.split()
    encrypted_words = [word[::-1] for word in words]
    encrypted_message = ' '.join(encrypted_words)

    with open('answer.txt', 'w', encoding='utf-8') as file:
        file.write(encrypted_message)

    print("Сообщение успешно зашифровано и записано в файл 'answer.txt'.")

else:
    print("Неверный выбор.")
