import nltk
from nltk import CFG, parse
grammar = CFG.fromstring("""
S -> NP VP
NP -> DT NN
VP -> VBZ NP
DT -> 'the'
NN -> 'cat' | 'dog'
VBZ -> 'chases' | 'sees'
""")
def parse_sentence(sentence, grammar):
    parser = parse.chart.ChartParser(grammar)
    return list(parser.parse(sentence.split()))
sentence = "the cat chases the dog"
print(parse_sentence(sentence, grammar))
