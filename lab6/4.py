'''Написать программу рисующую елочку с помощью символа ‘’. Высоту елочки пользователь вводит
с клавиатуры'''

n = int(input("Введите высоту елочки: "))

for i in range(1, n + 1):
    level = ' ' * (n - i) + '#' * (2 * i - 1)
    print(level)
print(' ' * (n - 1) + '#')
