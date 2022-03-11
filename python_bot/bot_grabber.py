from pyrogram import Client, filters
from datetime import datetime
import os
import sys
base_dir = os.path.abspath(os.path.join(os.path.dirname('bot_grabber.py'), '..'))
sys.path.append(base_dir)
from sql.sql import SQL

api_id = '18887197'
api_hash = '22f02b80d6e87e84fb25c236c5e5a15d'

app = Client('bot_python', api_id, api_hash)
bd = SQL('../bd.db')


@app.on_message(filters.chat(bd.get_donor()))
def get_post(client, message):
    username = message.chat.username
    message_id = message.message_id

    if not bd.message_id_exists(username, message_id):
        bd.add_message_id(username, message_id)
        # получение последнего ROWID
        for a in bd.get_last_rowid():
            last_id = a[0]

        # перессылка поста на модерку
        message.forward(bd.get_moder())
        client.send_message(bd.get_moder(), last_id)


@app.on_message(filters.chat(bd.get_moder()))
def send_post(client, message):
    # получаем запись в таблице
    for item in bd.get_data_in_table(message):
        username = item[0]
        msg_id = item[1]

    send = app.get_messages(username, msg_id)
    # send.forward(bd.get_channel(), as_copy=True)
    send.copy(bd.get_channel())


if __name__ == '__main__':
    print(datetime.today().strftime(f'%H:%M:%S | Bot Telegram-Grabber launched.'))
    app.run()
