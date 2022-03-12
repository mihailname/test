from telethon import TelegramClient, events
import asyncio

api_id = 18887197
api_hash = '22f02b80d6e87e84fb25c236c5e5a15d'

my_channel_id = -1001767381331
channels = [-1001758646521, -1001311684103, -1001080134301]

client = TelegramClient('myGrab', api_id, api_hash)
print("GRAB - Started")


@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message)
 
client.start()
client.run_until_disconnected()
