import spacy
from spacy.training import Example


class NLUProcessor:
    def __init__(self, model_dir):
        self.nlp = spacy.load(model_dir)

    def process_query(self, query):
        doc = self.nlp(query)
        if not doc.cats:
            raise ValueError("The model did not return any categories.")
        intent = max(doc.cats, key=doc.cats.get)
        entities = {ent.label_: ent.text for ent in doc.ents}
        return intent, entities
