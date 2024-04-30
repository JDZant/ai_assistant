import os
from ai_file_assistant.file_operations import search_files, create_file, delete_file

# Retrieve environment variables
APPLICATION_NAME = os.getenv('APPLICATION_NAME', 'AI Assistant')
DIR_PATH = os.getenv('DIR_PATH', '/home/jos/Desktop/files_for_ai')


def process_command(command):
    """Process a natural language command to perform file operations with a dynamic filename."""
    print(f"{APPLICATION_NAME} processing command: {command}")

    command_parts = command.split()
    if len(command_parts) < 3:
        print("Invalid command format. Expected format: [operation] file <filename>")
        return

    operation = command_parts[0]
    keyword = command_parts[1]
    filename = " ".join(command_parts[2:])

    if operation == 'create' and keyword == 'file' and filename:
        file_path = os.path.join(DIR_PATH, filename)
        create_file(file_path, 'Hello, world!')
        print(f"File created at {file_path}")

    elif operation == 'delete' and keyword == 'file' and filename:
        file_path = os.path.join(DIR_PATH, filename)
        delete_file(file_path)
        print(f"File deleted at {file_path}")

    elif operation == 'search' and keyword == 'file' and filename:
        # Use filename as the pattern to search for in the specified directory
        results = search_files(DIR_PATH, filename)
        if results:
            print("Files found:")
            for result in results:
                print(result)
        else:
            print("No files found matching your pattern.")

    else:
        print("Command not recognized.")


# Example usage of the function
process_command("search file example")
