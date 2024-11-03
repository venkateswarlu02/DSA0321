import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger_eng')
def pos_tagging(text):
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    return tagged_words
text = "NLTK is a powerful library for NLP."
print(pos_tagging(text))
