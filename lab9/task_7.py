'''Кинотеатр “Звездный” готовится к премьере долгожданного блокбастера. В зале n рядов по m мест
в каждом. Заказ билетов поступает онлайн, а информация о свободных местах хранится в виде
двумерного списка, где 1 - проданный билет, а 0 - свободное место.
Поступила группа из k зрителей, которые хотят сесть рядом в одном ряду.
Ваша задача:
Напишите программу, которая поможет кассиру “Звездного” определить, можно ли посадить эту
группу.
Ввод:
n - количество рядов в кинотеатре m - количество мест в ряду n строк с m числами (0 или 1),
разделенных пробелами - информация о занятости мест в каждом ряду k - количество билетов в
заказе
Вывод:
Номер ряда, в котором есть k подряд идущих свободных мест (номер ряда начинается с 1). Если
таких рядов несколько, то выведите номер наименьшего подходящего ряда. Если подходящего ряда
нет, выведите число 0.
'''

s = []
k = 0

n = int(input())

for i in range(n):
    s.append([])
    print(f"Введите {i+1} ряд: ")
    s[i].append("".join(input().split()))
    
x = int(input())
for j in s:
    k += 1
    if ("0"*x) in j[0]:
        print(k)
        break