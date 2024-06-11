import os
from query_processing.nlu_processor import NLUProcessor


class CommandController:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        model_name = "en_core_web_lg"
        self.nlu_processor = NLUProcessor(model_name)

    def handle_command(self, intent, entities):
        print(f"Intent: {intent}, Entities: {entities}")
        filename = entities.get('FILE_NAME', None)
        if not filename:  # Check if filename is extracted properly
            print("No filename provided. Please specify a file name.")
            return

        if intent == 'create_file':
            self.create_file(filename)
        elif intent == 'delete_file':
            self.delete_file(filename)
        elif intent == 'read_file':
            self.read_file(filename)
        else:
            print("No valid command recognized.")

    def create_file(self, filename):
        file_path = os.path.join(self.dir_path, filename)
        with open(file_path, 'w') as file:
            file.write('Hello, world!')
        print(f"File created at {file_path}")

    def delete_file(self, filename):
        file_path = os.path.join(self.dir_path, filename)
        try:
            os.remove(file_path)
            print(f"File deleted at {file_path}")
        except FileNotFoundError:
            print("File not found.")

    def read_file(self, filename):
        file_path = os.path.join(self.dir_path, filename)
        try:
            with open(file_path, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found.")
