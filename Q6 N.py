import random
def generate_bigram_model(text):
    words = text.split()
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    bigram_dict = {}
    for w1, w2 in bigrams:
        if w1 in bigram_dict:
            bigram_dict[w1].append(w2)
        else:
            bigram_dict[w1] = [w2]
    return bigram_dict
def generate_text(bigram_dict, start_word, length=10):
    current_word = start_word
    result = [current_word]
    for _ in range(length - 1):
        next_words = bigram_dict.get(current_word, None)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        current_word = next_word
    return ' '.join(result)
text = "the quick brown fox jumps over the lazy dog"
bigram_model = generate_bigram_model(text)
print(generate_text(bigram_model, "the"))
