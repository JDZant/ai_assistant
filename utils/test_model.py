import spacy


def test_model():
    nlp = spacy.load("./en_core_web_sm")
    texts = [
        "Create a file named birthday.txt",
        "Delete the file example.txt",
        "Read the file holiday.txt",
        "Read the file wedding.txt",
        "Create a document named report.txt",
        "Remove the file report.txt",
        "Open the file notes.txt",
        "Create a report named summary.doc",
        "Erase the document final_report.pdf",
        "Show me the document meeting_notes.docx",
        "Generate a new file called notes.txt",
        "Remove document final_summary.pdf",
        "Read the text file meeting_summary.doc",
        "Create new notes document named notes.txt",
        "Delete this file called old_notes.txt",
        "Open this document final_meeting.docx",
        "Make a file named holiday_plans.txt",
        "Erase the notes in old_report.txt",
        "Show the file named annual_summary.doc"
    ]
    for text in texts:
        doc = nlp(text)
        print(f"Text: {text}")
        print(f"Categories: {doc.cats}")
        print(f"Entities: {[(ent.text, ent.label_) for ent in doc.ents]}")
        print()


def test_create_file():
    nlp = spacy.load("./en_core_web_sm")  # Make sure to provide the correct path
    text = "Create a file named holiday_plans.txt"
    doc = nlp(text)
    print("Categories:", doc.cats)
    print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])


if __name__ == "__main__":
    # test_model()
    test_create_file()
