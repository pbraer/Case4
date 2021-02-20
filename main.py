# Case-study #4
# Developers:   Braer P. (%),
#               Kokorina D. (%),
#               Novoselov V. (%)
from textblob import TextBlob
import nltk
nltk.download('punkt')
t = input('Введите текст:')
txt = TextBlob(t)
print(len((txt.sentences)))
print(len((txt.words)))




