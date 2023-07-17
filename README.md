# Slack Message Extractor

This Python script retrieves messages from a public Slack channel using the Slack API and saves them to a JSON file.

## Prerequisites

- Python 3.x
- `slack_sdk` library (`pip install slack_sdk`)
- `python-dotenv` library (`pip install python-dotenv`)

## Getting Started

1. Clone the repository or download the script file (`slack_message_extractor.py`) to your local machine.

2. Install the required dependencies by running the following command:

    ```pip install -r requirements.txt```

3. Create a `.env` file in the same directory as the script file and set your Slack API token as follows:

    ```SLACK_API_TOKEN=<your_slack_api_token>```

4. Set the `channel_id` variable in the `main()` function to the ID of the public Slack channel you want to extract messages from.

5. Run the script:

    ```python slack_message_extractor.py```

The script will retrieve the messages from the specified Slack channel, replace user IDs with real names, extract reactions, and save the messages to a JSON file named `slack_messages.json`.

6. Once the script finishes executing, you can find the extracted messages in the `slack_messages.json` file.

## Customization

- You can modify the `extract_reactions()` function to extract additional information from message reactions if desired.

- The `save_to_json()` function allows you to specify a different file path or customize the JSON formatting if needed.

## Resources

- [Slack API Documentation](https://api.slack.com/)
- [slack_sdk Python Library Documentation](https://slack.dev/python-slack-sdk/)

## License

This project is licensed under the [MIT License](LICENSE).