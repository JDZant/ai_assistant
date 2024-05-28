import os
from dotenv import load_dotenv

# Load environment variables from .env file (if applicable)
load_dotenv()

from query_processing.nlu_processor import NLUProcessor
from controllers.command_controller import CommandController


def main():
    model_name = "en_core_web_sm"

    nlu_processor = NLUProcessor(model_name)
    command_controller = CommandController(os.getenv('DIR_PATH'))

    print(f"Working directory: {os.getenv('DIR_PATH')}")

    user_input = input("Please enter your command: ")
    intent, entities = nlu_processor.process_query(user_input)
    command_controller.handle_command(intent, entities)


if __name__ == "__main__":
    main()
