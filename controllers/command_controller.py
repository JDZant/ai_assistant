import os
from file_operations.file_operations import search_files, create_file, delete_file


class CommandController:
    """Handles processing of commands to perform file operations."""

    def __init__(self):
        self.application_name = os.getenv('APPLICATION_NAME', 'AI Assistant')
        self.dir_path = os.getenv('DIR_PATH', '/home/jos/Desktop/files_for_ai')

    def process_command(self, command):
        """Process a natural language command to perform file operations with a dynamic filename."""
        print(f"{self.application_name} processing command: {command}")

        command_parts = command.split()
        if len(command_parts) < 3:
            print("Invalid command format. Expected format: [operation] file <filename>")
            return

        operation = command_parts[0]
        keyword = command_parts[1]
        filename = " ".join(command_parts[2:])

        if operation == 'create' and keyword == 'file' and filename:
            self.create_file(filename)

        elif operation == 'delete' and keyword == 'file' and filename:
            self.delete_file(filename)

        elif operation == 'search' and keyword == 'file' and filename:
            self.search_file(filename)

        else:
            print("Command not recognized.")

    def create_file(self, filename):
        """Create a file in the specified directory."""
        file_path = os.path.join(self.dir_path, filename)
        create_file(file_path, 'Hello, world!')
        print(f"File created at {file_path}")

    def delete_file(self, filename):
        """Delete a file in the specified directory."""
        file_path = os.path.join(self.dir_path, filename)
        delete_file(file_path)
        print(f"File deleted at {file_path}")

    def search_file(self, filename):
        """Search for files using filename as the pattern in the specified directory."""
        results = search_files(self.dir_path, filename)
        if results:
            print("Files found:")
            for result in results:
                print(result)
        else:
            print("No files found matching your pattern.")

