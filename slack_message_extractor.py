import json
import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import dotenv_values

# Load environment variables from .env file
env_variables = dotenv_values('.env')

# Set your Slack API token
slack_token = env_variables["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

def extract_reactions(reactions):
    extracted_reactions = []
    for reaction in reactions:
        extracted_reactions.append({
            "name": reaction['name'],
            "count": reaction['count']
        })
    return extracted_reactions

def extract_messages(channel_id):
    try:
        response = client.conversations_history(channel=channel_id)
        messages = response['messages']
        while response['has_more']:
            response = client.conversations_history(
                channel=channel_id,
                cursor=response['response_metadata']['next_cursor']
            )
            messages.extend(response['messages'])
    except SlackApiError as e:
        print(f"Error retrieving messages: {e.response['error']}")
        return []

    extracted_messages = []
    for message in messages:
        user_info = client.users_info(user=message['user'])
        user_name = user_info['user']['real_name']

        # Replace user IDs with real names in the message
        tagged_users = re.findall(r'<@(.*?)>', message['text'])
        for user_id in tagged_users:
            user_info = client.users_info(user=user_id)
            user_name = user_info['user']['real_name']
            message['text'] = message['text'].replace(f'<@{user_id}>', user_name)

        extracted_messages.append({
            "person": user_name,
            "message": message['text'],
            "reactions": extract_reactions(message.get('reactions', [])),
            "reply_count": message.get('reply_count', 0)
        })
    return extracted_messages

def save_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    # Set the ID of the public Slack channel you want to read
    channel_id = 'C05HDDF3J1E'

    # Extract the messages from the channel
    messages = extract_messages(channel_id)

    # Save the messages to a JSON file
    save_to_json(messages, 'slack_messages.json')

if __name__ == '__main__':
    main()
