import spacy

nlp = spacy.load("en_core_web_sm")

def recognize_dialog_acts(dialogue):
    doc = nlp(dialogue)
    acts = []
    
    for sentence in doc.sents:
        if sentence.text.endswith('?'):
            acts.append((sentence.text, 'Question'))
        elif sentence.text.endswith('!'):
            acts.append((sentence.text, 'Exclamation'))
        else:
            acts.append((sentence.text, 'Statement'))
    
    return acts

dialogue = "Hello! How are you? I am fine."
print(recognize_dialog_acts(dialogue))
