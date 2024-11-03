import nltk
from nltk import CFG
grammar = CFG.fromstring("""
S -> NP VP
NP -> DT NN
VP -> VBZ NP | VBP NP
DT -> 'the' | 'a'
NN -> 'dog' | 'cat'
VBZ -> 'chases'
VBP -> 'chase'
""")
def check_agreement(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    parse_trees = list(parser.parse(sentence.split()))
    return parse_trees
sentence = "the dog chases the cat"
print(check_agreement(sentence, grammar))
