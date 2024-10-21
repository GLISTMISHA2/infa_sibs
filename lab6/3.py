'''По данному n вычислить y = 1^2 + 2^2 + ... + n
^2'''

n = int(input("Введите n: "))
res = 0
for i in range(1, n + 1):
    res = res + i ** 2

print("Результат: ",res)
