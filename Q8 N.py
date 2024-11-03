import random
class StochasticPOSTagger:
    def __init__(self, training_data):
        self.tag_probabilities = self.train(training_data)
    def train(self, training_data):
        tag_counts = {}
        word_tag_counts = {}  
        for sentence in training_data:
            for word, tag in sentence:
                if tag not in tag_counts:
                    tag_counts[tag] = 0
                tag_counts[tag] += 1                
                if word not in word_tag_counts:
                    word_tag_counts[word] = {}
                if tag not in word_tag_counts[word]:
                    word_tag_counts[word][tag] = 0
                word_tag_counts[word][tag] += 1
        total_tags = sum(tag_counts.values())
        tag_probabilities = {tag: count / total_tags for tag, count in tag_counts.items()}
        for word in word_tag_counts:
            for tag in word_tag_counts[word]:
                word_tag_counts[word][tag] /= tag_counts[tag]
        
        return tag_probabilities, word_tag_counts
    def tag(self, sentence):
        _, word_tag_counts = self.tag_probabilities
        tagged_sentence = []
        for word in sentence:
            if word in word_tag_counts:
                tag = max(word_tag_counts[word], key=word_tag_counts[word].get)
            else:
                tag = max(self.tag_probabilities[0], key=self.tag_probabilities[0].get)
            tagged_sentence.append((word, tag))
        return tagged_sentence
training_data = [[('the', 'DT'), ('dog', 'NN'), ('barks', 'VB')], [('a', 'DT'), ('cat', 'NN'), ('meows', 'VB')]]
tagger = StochasticPOSTagger(training_data)
sentence = "the cat meows"
print(tagger.tag(sentence.split()))
