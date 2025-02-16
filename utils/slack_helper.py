import traceback
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackNotifier:
    def __init__(self, bot_token: str, channel: str):
        #Initialize the Slack Client with the Bot Token
        #bot_token = os.getenv("BOT_TOKEN")
        self.client = WebClient(token=bot_token)
        self.channel = channel

    def send_message(self, channel: str, message: str):
        try:
            response = self.client.chat_postMessage(channel=channel, text=message)
            print(f"Message sent to {channel}: {response['message']['text']}")
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")

    def send_error_message(self, error_message: str, exception: Exception = None):
        error_text = f"*ERROR:* ```{error_message}```"

        if exception:
            error_trace = traceback.format_exc()  # Get the traceback
            error_text += f"\n*Traceback:*\n```{error_trace}```"
        self.send_message(self.channel, error_text)

