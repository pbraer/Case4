# Case-study #4
# Developers:   Braer P. 50(%),
#               Kokorina D. 50(%),
#               Novoselov V. 50(%)
import math
from textblob import TextBlob
from translate import Translator
t = input('Введите текст:')
txt = TextBlob(t)
t = t.lower()
vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'u', 'y', 'o']
translator = Translator(from_lang="russian", to_lang="english")
t1 = translator.translate(t)
t2 = t1.lower()
txt2 = TextBlob(t2)
lang = txt.detect_language()
vowel_txt = txt
sl = 0
for v in t:
    for let in vowel:
        if v == let:
            sl = sl + 1

ASL = (len(txt.words)/len(txt.sentences))
ASW = sl / len(txt.words)
print('Предложений:',len(txt.sentences))
print('Слов:',len(txt.words))
print('Средняя длина предложения в словах:', ASL)
print('Слогов:', sl)
print('Средняя длина слова в слогах:', ASW)
if lang == "ru":
    print('Объективность:',round(((1 - txt2.sentiment[1])*100),1), '%')
else:
    print('Объективность:',round(((1 - txt.sentiment[1])*100),1), '%')
if lang == "ru":
    analysisPol = TextBlob(t1).polarity
else:
    analysisPol = TextBlob(t).polarity
if -0.33 <= analysisPol <= 0.33:
    print('Тональность текста: нейтральный')
elif analysisPol < -0.33:
    print('Тональность текста: отрицательный')
elif analysisPol > 0.33:
    print('Тональность текста: положительный')
if lang == "ru":
    fre=206.835-(1.3 * ASL)-(60.1*ASW)
    print ("Индекс удобочитаемости Флеша:", fre)
    if fre > 80:
        print('Текст очень легко читается (для младших школьников).')
    elif 50 < fre <= 80:
        print('Простой текст (для школьников).')
    elif 25 < fre <= 50:
        print('Текст немного трудно читать (для студентов).')
    elif fre < 25:
        print('Текст трудно читается (для выпускников ВУЗов).')
else:
    fre = 206.835-(1.015 * ASL)-(84.6 * ASW)
    print("Индекс удобочитаемости Флеша:", fre)
    if fre > 80:
        print('Текст очень легко читается (для младших школьников).')
    elif 50 < fre <= 80:
        print('Простой текст (для школьников).')
    elif 25 < fre <= 50:
        print('Текст немного трудно читать (для студентов).')
    elif fre < 25:
        print('Текст трудно читается (для выпускников ВУЗов).')