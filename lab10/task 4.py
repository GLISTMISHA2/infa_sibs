# Запрашиваем у пользователя количество имен и пол
col = int(input("Введите количество имен: "))
gender = input("Введите гендер (М/Ж): ")

# Проверяем корректность ввода
if col <= 0 or gender not in "МмЖж":
    print("Неверные значения")
else:
    # Определяем файл для чтения в зависимости от пола
    if gender in "Мм":
        file_path = "file7.txt"
    else:
        file_path = "file8.txt"

    # Открываем файл для чтения
    with open(file_path, "r", encoding="utf8") as e:
        k = e.readlines()

    # Выводим первые col имен
    print(f"Топ {col} имен:")
    for i in range(col):
        print(k[i].split()[0])
