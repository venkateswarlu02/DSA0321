import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
def explore_wordnet(word):
    synsets = wordnet.synsets(word)
    result = []
    for synset in synsets:
        result.append({
            'name': synset.name(),
            'definition': synset.definition(),
            'examples': synset.examples()
        })
    return result
word = "bank"
print(explore_wordnet(word))
