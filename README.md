# CaRePi_slack
slack bot of **Ca**rd **Re**der de **Pi**tte suru yatsu

> [**CaRePi**](https://github.com/shmn7iii/CaRePi):  
> Composer of each system.
>
> [**CaRePi_api**](https://github.com/shmn7iii/CaRePi_api):  
> API program. Handle entry/exit and manage tokens. Ruby on Rails, tapyrusd
>
> [**CaRePi_reader**](https://github.com/shmn7iii/CaRePi_reader):  
> Card reader program. Read student number from student card and send request to API. Pyton, PaSoRi.
>
> [**CaRePi_slack**](https://github.com/motoha0827/CaRePi_slack):  
> Slack BOT program. Recieve slash command, interact with API, send message to Slack. Python, Slack BOLT.

## spec
Python 2.7.18

## setup
slackでソケットモードのアプリを作成して、トークンを生成しておきます。
それを.envに書きます。

必要なライブラリをインストールする。

```
$ pip install -r requirements.txt
```

ターミナルで以下のコマンドを入力し、アプリを立ち上げる。
```
$ python app.py
```
