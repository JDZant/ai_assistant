from query_processing.ai_interaction import query_mistral
from controllers.command_controller import CommandController


def main():
    controller = CommandController()
    user_input = input("Please enter your command: ")
    mistral_response = query_mistral(user_input)

    if mistral_response:
        controller.process_command(mistral_response)
    else:
        print("Failed to get a valid response from Mistral.")


if __name__ == "__main__":
    main()
