import spacy
nlp = spacy.load("en_core_web_sm")

def resolve_references(text):
    doc = nlp(text)
    for token in doc:
        if token.dep_ == 'nsubj' and token.head.pos_ == 'VERB':
            subj_verb = (token, token.head)
            break
    else:
        subj_verb = (None, None)
    
    return subj_verb

text = "John saw a dog and he liked it"
print(resolve_references(text))
