import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import datetime
import requests
import re

load_dotenv()

app = App(token=os.environ['SLACK_BOT_TOKEN'])

@app.command("/carepi")
def handle_carepi_command(ack, say, command):
    ack()
    user_id = command["user_id"]
    display_name = app.client.users_info(user=user_id)['user']['profile']['display_name']

    check_name = re.match(r'[0-9]{2}[A-Z][0-9]{3}.*', display_name)
    if check_name != None:
      student_num = display_name[:2] + "11140" + display_name[3:6]
      response = requests.post(f'http://localhost:3000/session?student_number={student_num}&no_send_slack=true')
      say(f'{response.json()["data"]} \n {command["text"]}')
    else:
      say('【ERROR】\n表示名を 入学年度 + J + 学籍番号下３桁 + 名字 の形式にしてください。(例:20J062秋本)')

if __name__ == '__main__':
  SocketModeHandler(app, os.environ['SLACK_APP_TOKEN']).start()
