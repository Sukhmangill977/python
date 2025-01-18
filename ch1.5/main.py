import requests
import json

# Cleverbot API URL
CLEVERBOT_API_URL = "https://www.cleverbot.com/getreply"

# Replace with your own Cleverbot API key (sign up on Cleverbot to get one)
API_KEY = "your_cleverbot_api_key"

def talk_to_cleverbot(user_input, conversation_id=None):
    # Prepare the data to be sent to the API
    data = {
        'key': API_KEY,
        'input': user_input,
        'cs': conversation_id,
    }

    # Send the request to the Cleverbot API
    response = requests.get(CLEVERBOT_API_URL, params=data)

    # Parse the response
    response_data = response.json()
    
    # Get the conversation ID and response from Cleverbot
    conversation_id = response_data.get('cs')
    bot_response = response_data.get('output')

    return bot_response, conversation_id


def main():
    print("Welcome to the Cleverbot chat!")
    print("You can start chatting with Cleverbot now.")
    
    conversation_id = None
    
    while True:
        # Get user input
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Ending the conversation. Goodbye!")
            break

        # Send user input to Cleverbot and get the response
        bot_response, conversation_id = talk_to_cleverbot(user_input, conversation_id)

        # Display the response
        print(f"Cleverbot: {bot_response}")

if __name__ == "__main__":
    main()
