def load_data():
    return [
        ("Create a file named birthday.txt", {"cats": {"create_file": 1.0}, "entities": [(20, 32, "FILE_NAME")]}),
        ("Delete the file example.txt", {"cats": {"delete_file": 1.0}, "entities": [(16, 27, "FILE_NAME")]}),
        ("Make a file named holiday_plans.txt", {
            "cats": {"create_file": 1.0, "delete_file": 0.0, "read_file": 0.0},
            "entities": [(20, 39, "FILE_NAME")]
        }),
        ("Read the file wedding.txt", {"cats": {"read_file": 1.0}, "entities": [(14, 25, "FILE_NAME")]}),
        ("Create a document named report.txt", {"cats": {"create_file": 1.0}, "entities": [(24, 34, "FILE_NAME")]}),
        ("Remove the file report.txt", {"cats": {"delete_file": 1.0}, "entities": [(16, 26, "FILE_NAME")]}),
        ("Open the file notes.txt", {"cats": {"read_file": 1.0}, "entities": [(14, 23, "FILE_NAME")]}),
        ("Create a report named summary.doc", {"cats": {"create_file": 1.0}, "entities": [(21, 33, "FILE_NAME")]}),
        ("Erase the document final_report.pdf", {"cats": {"delete_file": 1.0}, "entities": [(17, 35, "FILE_NAME")]}),
        ("Show me the document meeting_notes.docx", {"cats": {"read_file": 1.0}, "entities": [(19, 39, "FILE_NAME")]}),
        ("Generate a new file called notes.txt", {"cats": {"create_file": 1.0}, "entities": [(27, 36, "FILE_NAME")]}),
        ("Remove document final_summary.pdf", {"cats": {"delete_file": 1.0}, "entities": [(15, 33, "FILE_NAME")]}),
        ("Read the text file meeting_summary.doc", {"cats": {"read_file": 1.0}, "entities": [(19, 38, "FILE_NAME")]}),
        ("Create new notes document named notes.txt",
         {"cats": {"create_file": 1.0}, "entities": [(30, 39, "FILE_NAME")]}),
        ("Delete this file called old_notes.txt", {"cats": {"delete_file": 1.0}, "entities": [(27, 39, "FILE_NAME")]}),
        ("Open this document final_meeting.docx", {"cats": {"read_file": 1.0}, "entities": [(21, 39, "FILE_NAME")]}),
        ("Make a file named holiday_plans.txt", {"cats": {"create_file": 1.0}, "entities": [(18, 35, "FILE_NAME")]}),
        ("Erase the notes in old_report.txt", {"cats": {"delete_file": 1.0}, "entities": [(21, 33, "FILE_NAME")]}),
        ("Show the file named annual_summary.doc", {"cats": {"read_file": 1.0}, "entities": [(19, 37, "FILE_NAME")]}),
    ]
