'''Недавно Юра поступил в университет. У Юры есть друг Леша, который поступил вместе с ним, и
теперь они заселяются в общежитие.
Юра и Леша хотят жить в одной комнате. Всего в общежитии есть n комнат. В данный момент
в комнате с номером i живут pi человек, когда всего в этой комнате может жить qi человек (pi <=
qi). Посчитайте, сколько комнат общежития смогут вместить Юру и Лешу вместе?
Входные данные В первой строке содержится единственное целое число n (1 <= n <= 100) —
количество комнат.
В i-й из n последующих строк содержатся два целых числа pi и qi (0 <= pi <= qi <= 100) —
количество людей, которые уже живут в комнате, и максимальное допустимое количество людей,
живущих в i-й комнате.
Выходные данные Выведите одно целое число — количество комнат, в которые Юра с Лешей
могут заселиться'''

n = int(input())
count=0

for i in range(n):
    pi_str, qi_str = input().split()
    pi = int(pi_str)
    qi = int(qi_str)

    if qi - pi >= 2:
        count += 1

print(count)
