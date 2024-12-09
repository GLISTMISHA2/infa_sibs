# Запрашиваем у пользователя новую строку
new_line = input("Введите новую строку: ")

# Открываем файл для чтения
with open('file.txt', 'r', encoding='utf-8') as file:
    # Считываем все строки из файла
    lines = file.readlines()

# Определяем середину файла
middle_index = len(lines) // 2

# Вставляем новую строку в середину
lines.insert(middle_index, new_line + '\n')

# Открываем файл для записи
with open('file.txt', 'w', encoding='utf-8') as file:
    # Записываем обновленное содержимое обратно в файл
    file.writelines(lines)

print("Строка успешно добавлена в середину файла.")
