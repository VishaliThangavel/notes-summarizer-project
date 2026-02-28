import spacy

nlp = spacy.load("en_core_web_sm")

def extract_concepts(text):
    doc = nlp(text)
    
    concepts = []
    
    for ent in doc.ents:
        concepts.append(ent.text)
    
    return list(set(concepts))