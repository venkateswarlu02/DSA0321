import nltk
from nltk.tag import brill, brill_trainer, UnigramTagger, BigramTagger
from nltk.corpus import treebank
nltk.download('treebank')
training_data = treebank.tagged_sents()[:3000]
testing_data = treebank.tagged_sents()[3000:]
unigram_tagger = UnigramTagger(training_data)
bigram_tagger = BigramTagger(training_data, backoff=unigram_tagger)
def transformation_rule(tagging):
    transformations = [
        brill.Template(brill.Pos([-1])), 
        brill.Template(brill.Pos([1])),
        brill.Template(brill.Pos([1,1])),
        brill.Template(brill.Pos([-1,1]))
    ]
    trainer = brill_trainer.BrillTaggerTrainer(bigram_tagger, transformations)
    brill_tagger = trainer.train(tagging)
    return brill_tagger
brill_tagger = transformation_rule(training_data)
print(brill_tagger.accuracy(testing_data))
