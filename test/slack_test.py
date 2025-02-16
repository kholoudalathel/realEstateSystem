from utils.slack_helper import SlackNotifier
from utils import error_msgs
import os

slack_bot_token = os.getenv('SLACK_BOT_TOKEN')
slack_channel = os.getenv('SLACK_CHANNEL')

if not slack_bot_token or not slack_channel:
    raise ValueError("SLACK_BOT_TOKEN or SLACK_CHANNEL is missing! Set them before running.")

slack_notifier = SlackNotifier(slack_bot_token, slack_channel)

try:
    raise ConnectionError("Timeout while connecting to PostgreSQL")
except Exception as e:
    slack_notifier.send_error_message(
        error_msgs.POSTGRES_DB_CONNECTION_ERROR.format("Timeout while connecting"), e)