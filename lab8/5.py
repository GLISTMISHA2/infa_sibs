'''Андрей перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в
строю. Помогите ему это сделать. Программа получает на вход невозрастающую последовательность
натуральных чисел, означающих рост каждого человека в строю. После этого вводится число X —
3
рост Андрея. Все числа во входных данных натуральные и не превышают 230. Выведите номер, под
которым Андрей должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же,
как у Андрея, то он должен встать после них.'''

heights = input("введите рост каждого человека в строю : ").split()

heights = list(map(int, heights))# строки в целые числа

a_height = int(input("введите рост Андрея: "))

pos = 0
for i in heights:
    if a_height > i:
        break
    pos += 1

print("Андрей должен встать на позицию ", pos + 1)