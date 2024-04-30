import os


def search_files(directory, pattern):
    """Search for files that contain the pattern within their names in the specified directory."""
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if pattern.lower() in file.lower():
                matching_files.append(os.path.join(root, file))
    return matching_files


def create_file(file_path, content=''):
    """Create a file at the specified path and write content to it."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"File created: {file_path}")


def delete_file(file_path):
    """Delete the file at the specified path."""
    os.remove(file_path)
    print(f"File deleted: {file_path}")
