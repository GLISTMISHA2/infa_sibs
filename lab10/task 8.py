# Ввод данных
n, m = map(int, input("Введите n и m: ").split())

# Создаем пустую таблицу
table = [['.' for _ in range(m)] for _ in range(n)]

# Заполняем таблицу узором змейки
for i in range(0, n, 2):
    # Заполняем строку символами '#'
    table[i] = ['#'] * m

    # Если это не последняя строка, заполняем следующую строку
    if i + 1 < n:
        if (i // 2) % 2 == 0:
            table[i + 1][-1] = '#'
        else:
            table[i + 1][0] = '#'

# Выводим таблицу
for row in table:
    print(''.join(row))
