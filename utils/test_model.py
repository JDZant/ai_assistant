import spacy

def test_model():
    nlp = spacy.load("en_core_web_sm")
    texts = [
        "Create a file named birthday.txt",
        "Delete the file example.txt",
        "Read the file holiday.txt",
        "Read the file wedding.txt",
        "Create a document named report.txt",
        "Remove the file report.txt",
        "Open the file notes.txt"
    ]
    for text in texts:
        doc = nlp(text)
        print(f"Text: {text}")
        print(f"Categories: {doc.cats}")
        print(f"Entities: {[(ent.text, ent.label_) for ent in doc.ents]}")
        print()

if __name__ == "__main__":
    test_model()
