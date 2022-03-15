from telethon.sync import TelegramClient, events
from telethon.tl.types import Channel
import asyncio

api_id = 18887197
api_hash = '22f02b80d6e87e84fb25c236c5e5a15d'
my_channel_id = -1001764543059
channels = [-1001080134301, -1001758646521]
BADTEXT = {'t.me', 'http', 'подписаться', '@', 'joinchat', 'https'}
client = TelegramClient('myGrab', api_id, api_hash)

print("GRAB - Started")

def to_lower(word: str):
    return word.lower()

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event: events.newmessage.NewMessage.Event):
    global BADTEXT
    message_text = event.raw_text
    message_text_lowered = event.raw_text.lower()
    if event.message and not event.grouped_id and not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
        await asyncio.sleep(1)
        await client.send_message(my_channel_id, event.message)
 
@client.on(events.Album(chats=channels))
async def handler(event):
    
    message_text = event.raw_text
    message_text_lowered = event.raw_text.lower()
    if not [element for element in BADTEXT if message_text_lowered.__contains__(element)]:
        await asyncio.sleep(1)
        await client.send_message(my_channel_id,file=event.messages,message=event.original_update.message.message,)
client.start()
client.run_until_disconnected()
