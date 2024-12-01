'''В известной игре Эрудит каждой букве соответствует определенное количество очков. Общая сумма
очков, которую получает игрок, составивший это слово, складывается из очков за каждую букву,
входящую в его состав. Чем более употребимой является буква в языке, тем меньше очков начисляется за ее использование.
Напишите программу, рассчитывающую и отображающую количество очков за собранное слово.
Создайте словарь для хранения соответствий между буквами и очками и используйте его в своем
решении.'''

s = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

word = input("Введите слово: ")
word = word.upper()

point = 0
for i in word:
    if i in s:
        point += s[i]

print(f"Количество очков за слово '{word}': {point}")