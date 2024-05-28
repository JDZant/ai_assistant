import spacy
from spacy.training import Example


def load_data():
    return [
        ("Create a file named report.txt", {
            "intent": "create_file",
            "entities": [
                ("report.txt", "FILE_NAME")
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
        example = Example.from_dict(doc, {'cats': annotations})
        nlp.update([example])

    nlp.to_disk("en_core_web_md")


if __name__ == "__main__":
    training_data = load_data()
    train_nlu_model(training_data)
