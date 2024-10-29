'''Довольно распространённая ошибка ошибка – это повтор слова. Вот в предыдущем предложении
такая допущена. Необходимо исправить каждый такой повтор. Повтор это – слово , ТОЛЬКО один
пробел, и снова то же слово.
'''
text = input()
words = text.split()
fix_words = []
prev_word = None

for word in words:
    if word != prev_word:
        fix_words.append(word)
    prev_word = word

fix_text = ' '.join(fix_words)
print(fix_text)
