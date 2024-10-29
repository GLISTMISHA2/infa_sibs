
line1 = input("Введите первую строку: ")
line2 = input("Введите вторую строку: ")
line3 = input("Введите третью строку: ")

if (line1 and line2 and line3):
    slova = "аеёиоуыэюя"
    count1 = sum(1 for char in line1 if char.lower() in slova) 
  '''for char in line1:
    if char.lower() in slova:
        count1 += 1'''
    count2 = sum(1 for char in line2 if char.lower() in slova)
    count3 = sum(1 for char in line3 if char.lower() in slova)

    if count1 == 5 and count2 == 7 and count3 == 5:
        print("Хайку!")
    else:
        print("Не хайку.")    
else:
    print("Не хайку. Должно быть 3 строки.")
