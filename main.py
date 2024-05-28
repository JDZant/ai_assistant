import os
from dotenv import load_dotenv
from query_processing.nlu_processor import NLUProcessor
from controllers.command_controller import CommandController

# Load environment variables from .env file
load_dotenv()


def main():
    model_dir = "en_core_web_sm"

    nlu_processor = NLUProcessor(model_dir)
    command_controller = CommandController(os.getenv('DIR_PATH'))

    print(f"Working directory: {os.getenv('DIR_PATH')}")

    user_input = input("Please enter your command: ")
    try:
        intent, entities = nlu_processor.process_query(user_input)
        command_controller.handle_command(intent, entities)
    except ValueError as e:
        print(f"Error processing query: {e}")


if __name__ == "__main__":
    main()
