'''Напишите программу, которая будет запрашивать у пользователя числа, пока он не пропустит ввод.
Сначала на экран должно быть выведено среднее значение введенного ряда чисел, после этого друг
за другом необходимо вывести список чисел ниже среднего, равных ему (если такие найдутся) и
выше среднего. Каждый список должен предваряться соответствующим заголовком.'''

nums = []
total = 0
count = 0

print("введите числа :")

while True:
    uinput = input()
    if uinput == "":
        break
    try:
        number = float(uinput)
        nums.append(number)
        total += number
        count += 1
    except ValueError:
        print("ошибка")

if count > 0:
    average = total / count
    print("среднее значение чисел: ", average)

    nize = []
    rav = []
    vise = []

    for number in nums:
        if number < average:
            nize.append(number)
        elif number == average:
            rav.append(number)
        else:
            vise.append(number)

    print("ниже среднего:")
    print(nize)

    if rav:
        print("равные среднему:")
        print(rav)

    print("выше среднего:")
    print(vise)
else:
    print("не ввели ни одного числа.")#1 3 5 7 2 8 
