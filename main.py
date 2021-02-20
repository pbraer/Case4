# Case-study #4
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)
from textblob import TextBlob
t = input('Введите текст:')
txt = TextBlob(t)
print(len((txt.sentences)))