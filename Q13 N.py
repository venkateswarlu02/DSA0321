import nltk
from nltk import CFG
grammar = CFG.fromstring("""
S -> NP VP
NP -> DT NN
VP -> VBZ NP
DT -> 'the'
NN -> 'cat' | 'dog'
VBZ -> 'chases' | 'sees'
""")
def generate_parse_tree(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    parse_trees = list(parser.parse(sentence.split()))
    for tree in parse_trees:
        print(tree)
        tree.draw()
sentence = "the cat chases the dog"
generate_parse_tree(sentence, grammar)
