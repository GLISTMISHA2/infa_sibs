'''Количество дней в месяце варьируется от 28 до 31. Очередная ваша программа должна запрашивать у пользователя название месяца и отображать количество дней в нем. Поскольку года мы не
учитываем, для февраля можно вывести сообщение о том, что этот месяц может состоять как из 28,
так и из 29 дней, чтобы учесть фактор високосного года.'''

m = input("Введите название месяца: ")

if m in ["январь", "март", "май", "июль", "август", "октябрь", "декабрь"]:
    print("31 день")
elif m in ["апрель", "июнь", "сентябрь", "ноябрь"]:
    print("30 дней")
elif m == "февраль":
    print("28 или 29 дней")
else:
    print("Неверное название месяца")
