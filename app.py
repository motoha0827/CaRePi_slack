import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import datetime
import requests

load_dotenv()

app = App(token=os.environ['SLACK_BOT_TOKEN'])

@app.command("/carepi")
def handle_carepi_command(ack, say, command):
    ack()
    name = command["user_name"]
    sn = name[:1] + "11140" + name[3:6]
    print(sn)

if __name__ == '__main__':
  SocketModeHandler(app, os.environ['SLACK_APP_TOKEN']).start()
