# Открываем первый файл для чтения
with open("file5.txt", "r", encoding="utf8") as e1:
    k1 = e1.readlines()

# Открываем второй файл для чтения
with open("file6.txt", "r", encoding="utf8") as e2:
    k2 = e2.readlines()

# Инициализируем флаги
found_in_file5 = False
found_in_file6 = False

# Проверяем наличие слова "Academy" в первом файле
for line in k1:
    if "Academy" in line:
        found_in_file5 = True
        break

# Проверяем наличие слова "Academy" во втором файле
for line in k2:
    if "Academy" in line:
        found_in_file6 = True
        break

# Выводим результат
if found_in_file5 and found_in_file6:
    print("Слово 'Academy' найдено в обоих файлах.")
elif found_in_file5:
    print("Слово 'Academy' найдено в файле file5.txt.")
elif found_in_file6:
    print("Слово 'Academy' найдено в файле file6.txt.")
else:
    print("Слово 'Academy' не найдено ни в одном из файлов.")
