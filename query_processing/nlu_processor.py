import spacy
from spacy.training import Example


class NLUProcessor:
    def __init__(self, model_name):
        self.nlp = spacy.load(model_name)

    def process_query(self, query):
        doc = self.nlp(query)
        intent = max(doc.cats, key=doc.cats.get)
        entities = {ent.label_: ent.text for ent in doc.ents}
        return intent, entities


def load_data():
    return [
        ("Create a file named report.txt", {
            "cats": {"create_file": 1.0},
            "entities": [
                {"start": 17, "end": 27, "label": "FILE_NAME"}
            ]
        }),
    ]


def train_nlu_model(data):
    nlp = spacy.blank('en')
    textcat = nlp.add_pipe('textcat_multilabel')
    textcat.add_label("create_file")
    # Add more labels

    for text, annotations in data:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, {'cats': annotations['cats'], 'entities': annotations['entities']})
        nlp.update([example])

    model_name = "en_core_web_sm"
    nlp.to_disk(model_name)


if __name__ == "__main__":
    training_data = load_data()
    train_nlu_model(training_data)
