import spacy


def verify_offsets(text, entities):
    nlp = spacy.blank('en')
    doc = nlp.make_doc(text)
    for start, end, label in entities:
        span = doc.char_span(start, end, label=label)
        if span is None:
            print(f"Entity '{text[start:end]}' at offsets ({start}, {end}) could not be aligned.")
        else:
            print(
                f"Entity '{span.text}' aligned correctly as {span.label_} at offsets ({span.start_char}, {span.end_char}).")


def main():
    data = [
        ("Create a file named birthday.txt", [(20, 32, "FILE_NAME")]),
        ("Delete the file example.txt", [(16, 27, "FILE_NAME")]),
        ("Read the file holiday.txt", [(14, 25, "FILE_NAME")]),
        ("Read the file wedding.txt", [(14, 25, "FILE_NAME")]),
        ("Read the file report.txt", [(14, 24, "FILE_NAME")]),
        ("Read the file notes.txt", [(14, 23, "FILE_NAME")]),
    ]

    for text, entities in data:
        print(f"\nText: {text}")
        verify_offsets(text, entities)


if __name__ == "__main__":
    main()
