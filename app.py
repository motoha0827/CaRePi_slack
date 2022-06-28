# coding: UTF-8
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import requests
import re

load_dotenv()
app = App(token=os.environ['SLACK_BOT_TOKEN'])
api_endpoint = os.environ['API_ENDPOINT']


@app.command("/carepi")
def handle_carepi_command(ack, say, command):
    ack()
    user_id = command["user_id"]
    channel_id = command["channel_id"]
    display_name = app.client.users_info(
        user=user_id)['user']['profile']['display_name']
    ephemeral_text = '【ERROR】\n表示名を 学籍番号 + 名字 の形式にしてください。(例:2011140062秋本)'

    check_name = re.match(r'[0-9]{10}.*', display_name)
    if check_name != None:
        student_num = display_name[:10]
        response = requests.post(
            api_endpoint, data={'student_number': student_num})
        say(f'{response.json()["data"]} \n {command["text"]}')
    else:
        app.client.chat_postEphemeral(
            channel=channel_id, text=ephemeral_text, user=user_id)


if __name__ == '__main__':
    SocketModeHandler(app, os.environ['SLACK_APP_TOKEN']).start()
