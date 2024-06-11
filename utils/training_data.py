def load_data():
    return [
        ("Create a file named birthday.txt", {"cats": {"create_file": 1.0}, "entities": [(20, 32, "FILE_NAME")]}),
        ("Delete the file example.txt", {
            "cats": {"delete_file": 1.0, "create_file": 0.0},
            "entities": [(16, 27, "FILE_NAME")]
        }),
        ("Make a file named holiday_plans.txt", {
            "cats": {"create_file": 1.0, "delete_file": 0.0, "read_file": 0.0},
            "entities": [(18, 35, "FILE_NAME")]
        }),
        ("delete file a.txt", {
            "cats": {"create_file": 0.0, "delete_file": 1.0, "read_file": 0.0},
            "entities": [(12, 17, "FILE_NAME")]
        }),
        ("create file a.txt", {
            "cats": {"create_file": 1.0, "delete_file": 0.0, "read_file": 0.0},
            "entities": [(12, 17, "FILE_NAME")]
        }),
        ("read file a.txt", {
            "cats": {"create_file": 0.0, "delete_file": 0.0, "read_file": 1.0},
            "entities": [(10, 15, "FILE_NAME")]
        }),
        ("Read the file wedding.txt", {"cats": {"read_file": 1.0}, "entities": [(14, 25, "FILE_NAME")]}),
        ("Create a document named report.txt", {"cats": {"create_file": 1.0}, "entities": [(24, 34, "FILE_NAME")]}),
        ("Remove the file report.txt", {"cats": {"delete_file": 1.0}, "entities": [(16, 26, "FILE_NAME")]}),
        ("Open the file notes.txt", {"cats": {"read_file": 1.0}, "entities": [(14, 23, "FILE_NAME")]}),
        ("Create a report named summary.doc", {"cats": {"create_file": 1.0}, "entities": [(22, 33, "FILE_NAME")]}),
        ("Erase the document final_report.pdf", {"cats": {"delete_file": 1.0}, "entities": [(19, 35, "FILE_NAME")]}),
        ("Generate a new file called notes.txt", {"cats": {"create_file": 1.0}, "entities": [(27, 36, "FILE_NAME")]}),
        ("Read the text file meeting_summary.doc", {"cats": {"read_file": 1.0}, "entities": [(19, 38, "FILE_NAME")]}),
        ("Create new notes document named notes.txt",
         {"cats": {"create_file": 1.0}, "entities": [(32, 41, "FILE_NAME")]}),
        ("Delete this file called old_notes.txt", {"cats": {"delete_file": 1.0}, "entities": [(24, 37, "FILE_NAME")]}),
        ("Make a file named holiday_plans.txt", {"cats": {"create_file": 1.0}, "entities": [(18, 35, "FILE_NAME")]}),
        ("Erase the notes in old_report.txt", {"cats": {"delete_file": 1.0}, "entities": [(19, 33, "FILE_NAME")]}),
        ("Please create a new file called project_overview.docx",
         {"cats": {"create_file": 1.0}, "entities": [(32, 53, "FILE_NAME")]}),
        ("Can you read out the contents of memo.txt?",
         {"cats": {"read_file": 1.0}, "entities": [(33, 42, "FILE_NAME")]}),
        ("Generate a document titled annual_report.pdf",
         {"cats": {"create_file": 1.0}, "entities": [(27, 44, "FILE_NAME")]}),
        ("Delete the file old_database.db", {"cats": {"delete_file": 1.0}, "entities": [(16, 31, "FILE_NAME")]}),
        ("Create a backup named backup_2023.zip", {"cats": {"create_file": 1.0}, "entities": [(22, 37, "FILE_NAME")]}),
        ("Erase all files with the term project in their names", {"cats": {"delete_file": 1.0}, "entities": []}),

        # No specific file name
        ("Start a new file called sketch.svg", {"cats": {"create_file": 1.0}, "entities": [(24, 34, "FILE_NAME")]}),
        ("Access the record in file records.csv", {"cats": {"read_file": 1.0}, "entities": [(26, 37, "FILE_NAME")]}),
        ("Permanently delete the file draft_v1.doc",
         {"cats": {"delete_file": 1.0}, "entities": [(28, 40, "FILE_NAME")]}),
        ("Create a report named summary.doc", {"cats": {"create_file": 1.0}, "entities": [(22, 33, "FILE_NAME")]}),
        ("Create a file named image.jpeg", {"cats": {"create_file": 1.0}, "entities": [(20, 30, "FILE_NAME")]}),
        ("Can you delete the video.mp4?", {"cats": {"delete_file": 1.0}, "entities": [(19, 28, "FILE_NAME")]}),
        ("Make a file named holiday_plans.txt", {"cats": {"create_file": 1.0}, "entities": [(18, 35, "FILE_NAME")]}),
    ]
