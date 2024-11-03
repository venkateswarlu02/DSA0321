import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

def lesk_wsd(sentence, word):
    sense = lesk(word_tokenize(sentence), word)
    return sense.definition()

sentence = "I went to the bank to deposit money"
word = "bank"
print(lesk_wsd(sentence, word))
