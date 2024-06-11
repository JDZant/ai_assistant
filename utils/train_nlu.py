import random

import spacy
from spacy.training import Example
from pathlib import Path
from training_data import load_data


def train_nlu_model(data):
    nlp = spacy.blank('en')

    # Add text categorization pipeline component
    if "textcat_multilabel" not in nlp.pipe_names:
        textcat = nlp.add_pipe('textcat_multilabel', last=True)
    else:
        textcat = nlp.get_pipe("textcat_multilabel")

    textcat.add_label("create_file")
    textcat.add_label("delete_file")
    textcat.add_label("read_file")

    # Add entity recognizer to the pipeline, if needed
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe('ner', last=True)
    else:
        ner = nlp.get_pipe('ner')

    # Add new entity type to entity recognizer
    ner.add_label("FILE_NAME")

    # Begin training
    nlp.begin_training()
    for i in range(200):  # Increase iterations for more robust training
        random.shuffle(data)  # Randomize data at each iteration
        losses = {}
        for text, annotations in data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], sgd=nlp.create_optimizer(), losses=losses)
        print(f"Iteration {i} - Losses: {losses}")

    # Save the trained model
    model_dir = Path("en_core_web_sm")
    if not model_dir.exists():
        model_dir.mkdir()
    nlp.to_disk(model_dir)


if __name__ == "__main__":
    data = load_data()
    train_nlu_model(data)
