'''В данном задании вам предлагается реализовать простейший вариант игры "Морской бой". Дано
поле 4х4 и 4 однопалубных корабля, которые расставлены рандомно. Пользователю каждый раз
показывается поле:
. . . .
. . . .
. . . .
. . . .
и предлагается сделать выстрел (например, коррдината (1, 2))
Если он попал в корабль, то данная ячейка становится равной X
. X . .
. . . .
. . . .
. . . .
иначе поле остается без изменений.
Игра будет идти до тех пор, пока пользователь не нашел все корабли.
Но на поле присутствует одна бомба (B), при попадании на которую пользователь проигрывает.
Положение бобмы определяется рандомом.
При положительном исходе игры, попимо вывода поздравления, выведите за сколько шагов пользователь нашел все 4 корабля.'''

import random as r

s = [[".",".",".","."],
     [".",".",".","."],
     [".",".",".","."],
     [".",".",".","."]]
boats = []
st = 0
boat_count = 0
bomb = ""

while len(boats) < 4:
    k = str(r.randint(1,4))+str(r.randint(1,4))
    if k not in boats:
        boats.append(k)

while True:
    k = str(r.randint(1,4))+str(r.randint(1,4))
    if k not in boats:
        bomb += k
        break

while True:
    st += 1
    z = "".join(input().split())
    if z == bomb:
        print("Вы попали в бомбу")
        break
    if z in boats:
        s[int(z[0])-1][int(z[1])-1] = "X"
        boat_count += 1
    for i in s:
        print(" ".join(i))
    if boat_count == 4:
        print("Вы победили!")
        print(st)
        break
