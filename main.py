# Case-study #4
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)
from textblob import TextBlob
import nltk
t = input('Введите текст:')
txt = TextBlob(t)
print('Предложений:',len((txt.sentences)))
print('Слов:',len((txt.words)))
print('Средняя длина предложения в словах:',(len((txt.words))/len((txt.sentences))))
print('Объективность:',(1 - txt.sentiment[1]),'%')
