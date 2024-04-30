import os


def search_file_content(directory, content):
    """Search for specific content within text files in the specified directory."""
    content_found_in = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if content.lower() in f.read().lower():
                        content_found_in.append(file_path)
            except UnicodeDecodeError:
                continue  # This skips files that aren't text readable (e.g., binary files)
    return content_found_in
