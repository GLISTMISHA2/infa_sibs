'''Вы работаете в компании, которая занимается обработкой данных. Вам поступил список данных, в
котором перемешаны буквы и цифры. Разбейте этот список на два новых списка: один с буквами,
а второй с цифрами. После этого удалите исходный список и выведите на экран два новых списка,
каждый на отдельной строке.'''

a = input("Введите строку : ")
byk = []
dig = []

for item in a:
    if item.isdigit():  # цифрой
        dig.append(item)
    elif item.isalpha():  # буквой
        byk.append(item)

print(byk)
print(dig)