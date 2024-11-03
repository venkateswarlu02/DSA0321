import nltk
from nltk.grammar import Nonterminal, ProbabilisticProduction, PCFG
productions = """
    S -> NP VP [1.0]
    NP -> DT NN [0.5]
    NP -> NN [0.5]
    VP -> VBZ NP [0.5]
    VP -> VBP NP [0.5]
    DT -> 'the' [0.6]
    DT -> 'a' [0.4]
    NN -> 'dog' [0.5]
    NN -> 'cat' [0.5]
    VBZ -> 'chases' [1.0]
    VBP -> 'chase' [1.0]
"""
grammar = PCFG.fromstring(productions)
def probabilistic_parse(sentence, grammar):
    parser = nltk.ViterbiParser(grammar)
    parse_trees = list(parser.parse(sentence.split()))
    return parse_trees
sentence = "the dog chases a cat"
print(probabilistic_parse(sentence, grammar))
