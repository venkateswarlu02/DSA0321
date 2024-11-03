import nltk
from nltk import CFG
from nltk.parse import earleychart
grammar = CFG.fromstring("""
S -> NP VP
NP -> DT NN
VP -> VBZ NP
DT -> 'the'
NN -> 'cat' | 'dog'
VBZ -> 'chases' | 'sees'
""")
def earley_parse_sentence(sentence, grammar):
    parser = earleychart.EarleyChartParser(grammar)
    return list(parser.parse(sentence.split()))
sentence = "the cat chases the dog"
print(earley_parse_sentence(sentence, grammar))
