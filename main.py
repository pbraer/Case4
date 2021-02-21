# Case-study #4
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)
from textblob import TextBlob
import nltk
t = input('Введите текст:')
txt = TextBlob(t)
vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'u', 'y', 'o']
n = 0
print('Предложений:',len((txt.sentences)))
print('Слов:',len((txt.words)))
print('Средняя длина предложения в словах:',(len((txt.words))/len((txt.sentences))))
print('Объективность:',(1 - txt.sentiment[1]),'%')
for i in range(len(t)):
    if t[i] in vowel:
        n += 1
print('Слогов:', n)