import random
def generate_markov_model(text):
    words = text.split()
    model = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1] 
        if current_word not in model:
            model[current_word] = []
        model[current_word].append(next_word)
    return model
def generate_text(model, start_word, length=50):
    current_word = start_word
    text = [current_word]
    for _ in range(length - 1):
        if current_word not in model:
            break
        next_word = random.choice(model[current_word])
        text.append(next_word)
        current_word = next_word
    return ' '.join(text)
text = "the quick brown fox jumps over the lazy dog the lazy dog barks at the quick fox"
model = generate_markov_model(text)
start_word = "the"
generated_text = generate_text(model, start_word)
print(generated_text)
