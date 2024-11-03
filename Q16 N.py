import spacy
nlp = spacy.load("en_core_web_sm")
def named_entity_recognition(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities
text = "Apple is looking at buying U.K. startup for $1 billion"
print(named_entity_recognition(text))
