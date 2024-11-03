def evaluate_coherence(text):
    sentences = text.split('.')
    coherence_score = 0
    
    for i in range(1, len(sentences)):
        words_current = sentences[i].strip().split()
        words_previous = sentences[i-1].strip().split()
        
        if words_current and words_previous and words_current[0] == words_previous[-1]:
            coherence_score += 1
    
    return coherence_score

text = "The cat chased the mouse. The mouse ran away."
print(evaluate_coherence(text))
