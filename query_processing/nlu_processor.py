import spacy
from spacy.training import Example


class NLUProcessor:
    def __init__(self, model_dir):
        self.nlp = spacy.load(model_dir)

    def process_query(self, query):
        doc = self.nlp(query)
        print(doc)
        if not doc.cats:
            raise ValueError("The model did not return any categories.")
        # Select the category with the highest score that exceeds a threshold
        intent = max(doc.cats, key=lambda key: doc.cats[key]) if doc.cats else 'unknown'
        entities = {ent.label_: ent.text for ent in doc.ents}
        return intent, entities
