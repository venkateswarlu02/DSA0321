import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> DT NN
VP -> VBZ NP
DT -> 'the' | 'a'
NN -> 'dog' | 'cat'
VBZ -> 'sees' | 'chases'
""")

def extract_noun_phrases(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    parse_trees = list(parser.parse(sentence.split()))
    noun_phrases = []
    
    for tree in parse_trees:
        for subtree in tree.subtrees():
            if subtree.label() == 'NP':
                noun_phrases.append(" ".join(subtree.leaves()))
    return noun_phrases

sentence = "the cat sees the dog"
print(extract_noun_phrases(sentence, grammar))
