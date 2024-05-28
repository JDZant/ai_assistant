import spacy
from spacy.training import Example
from pathlib import Path

def load_data():
    return [
        ("Create a file named birthday.txt", {
            "cats": {"create_file": 1.0},
            "entities": [
                (20, 32, "FILE_NAME")
            ]
        }),
        ("Delete the file example.txt", {
            "cats": {"delete_file": 1.0},
            "entities": [
                (16, 27, "FILE_NAME")
            ]
        }),
        ("Read the file holiday.txt", {
            "cats": {"read_file": 1.0},
            "entities": [
                (14, 25, "FILE_NAME")
            ]
        }),
        ("Read the file wedding.txt", {
            "cats": {"read_file": 1.0},
            "entities": [
                (14, 25, "FILE_NAME")
            ]
        }),
        ("Create a document named report.txt", {
            "cats": {"create_file": 1.0},
            "entities": [
                (24, 34, "FILE_NAME")
            ]
        }),
        ("Remove the file report.txt", {
            "cats": {"delete_file": 1.0},
            "entities": [
                (16, 26, "FILE_NAME")
            ]
        }),
        ("Open the file notes.txt", {
            "cats": {"read_file": 1.0},
            "entities": [
                (14, 23, "FILE_NAME")
            ]
        }),
    ]

def train_nlu_model(data):
    nlp = spacy.blank('en')

    if "textcat_multilabel" not in nlp.pipe_names:
        textcat = nlp.add_pipe('textcat_multilabel', last=True)
    else:
        textcat = nlp.get_pipe("textcat_multilabel")

    textcat.add_label("create_file")
    textcat.add_label("delete_file")
    textcat.add_label("read_file")

    optimizer = nlp.begin_training()
    for i in range(10):  # Number of iterations
        losses = {}
        for text, annotations in data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, {"cats": annotations["cats"], "entities": annotations["entities"]})
            print(f"Training with example: {doc.text}, {annotations['cats']}, {annotations['entities']}")
            nlp.update([example], sgd=optimizer, losses=losses)
        print(f"Iteration {i} - Losses: {losses}")

    model_dir = Path("en_core_web_sm")
    if not model_dir.exists():
        model_dir.mkdir()
    nlp.to_disk(model_dir)

if __name__ == "__main__":
    training_data = load_data()
    train_nlu_model(training_data)
