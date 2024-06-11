import os
from dotenv import load_dotenv
from query_processing.nlu_processor import NLUProcessor
from controllers.command_controller import CommandController

# Load environment variables from .env file
load_dotenv()


def main():
    model_dir = "utils/en_core_web_sm"

    nlu_processor = NLUProcessor(model_dir)
    dir_path = os.getenv('DIR_PATH')
    if not dir_path:
        raise EnvironmentError(
            "Environment variable 'DIR_PATH' is not set. Please set this variable in your .env file.")

    print(f"Working directory: {dir_path}")

    while True:  # This loop will keep the program running, asking for new commands
        user_input = input("Please enter your command or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting the application.")
            break

        try:
            intent, entities = nlu_processor.process_query(user_input)
            command_controller = CommandController(dir_path)
            command_controller.handle_command(intent, entities)
        except ValueError as e:
            print(f"Error processing query: {e}")


if __name__ == "__main__":
    main()
