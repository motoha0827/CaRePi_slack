import os
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import datetime

load_dotenv()

app = App(token=os.environ['SLACK_BOT_TOKEN'])

if __name__ == '__main__':
  SocketModeHandler(app, os.environ['SLACK_APP_TOKEN']).start()
