'''Дана квадратная матрица n x n. Поменяйте местами элементы, стоящие на главной и побочной
диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце
нужно поменять местами элемент на главной диагонали и на побочной диагонали).
Входные данные:
n - количество строк и столбцов
и сама матрица вводится с клавиатуры'''

n = int(input())
s = []
k = n - 1

for i in range(n):
    s.append(input().split())

for i in range(n):
    z = s[i][i]
    s[i][i] = s[k][i]
    s[k][i] = z
    k = k - 1

for j in s:
    print(" ".join(j))
