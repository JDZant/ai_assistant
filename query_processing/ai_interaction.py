import subprocess


def query_mistral(query):
    """Send a query to Mistral using Ollama and return the response via stdin."""
    try:
        # Set up the command to run Mistral with Ollama
        command = ['ollama', 'run', 'mistral']
        # Execute the command and pass the query via stdin
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True)
        stdout, stderr = process.communicate(input=query)

        if process.returncode == 0:
            return stdout.strip()  # Assuming the response is in plain text
        else:
            print("Error in calling Mistral:", stderr)
            return None
    except Exception as e:
        print("Failed to run Mistral command:", e)
        return None
