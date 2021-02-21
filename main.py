# Case-study #4
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)
from textblob import TextBlob
from translate import Translator
t = input('Введите текст:')
txt = TextBlob(t)
vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'u', 'y', 'o']
n = 0
translator = Translator(from_lang="russian", to_lang="english")
t1 = translator.translate(t)
t2 = t1.lower()
print('Предложений:',len((txt.sentences)))
print('Слов:',len((txt.words)))
print('Средняя длина предложения в словах:', (len((txt.words))/len((txt.sentences))))
print('Объективность:',(1 - txt.sentiment[1]), '%')
for i in range(len(t)):
    if t[i] in vowel:
        n += 1
print('Слогов:', n)
l_word = n / len((txt.words))
print('Средняя длина слова в слогах:', l_word)
analysisPol = TextBlob(t2).polarity
if analysisPol == 0:
    print('Тональность текста: нейтральный')
elif analysisPol < 0:
    print('Тональность текста: отрицательный')
elif analysisPol > 0:
    print('Тональность текста: положительный')
