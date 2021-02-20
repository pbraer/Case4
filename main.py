# Case-study #4
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)
from textblob import TextBlob
t = input('Введите текст:')
txt = TextBlob(t)
sent = TextBlob.sentences(t)
print(sent)