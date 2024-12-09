# Открываем файл для чтения
with open("file6.txt", "r", encoding="utf8") as e:
    k = e.readlines()

# Инициализируем счетчики
count_vsego = 0
count_e = 0

# Проходим по каждой строке файла
for i in k:
    # Разделяем строку на слова по пробелам
    words = i.split()
    for word in words:
        count_vsego += 1
        # Проверяем, содержит ли слово букву 'e' или 'E'
        if 'e' in word.lower():
            count_e += 1

# Вычисляем процент слов, содержащих букву 'e'
percentage_with_e = (count_e / count_vsego) * 100

# Выводим результат
print(f"Процент слов, содержащих букву 'e': {percentage_with_e:.2f}%")
