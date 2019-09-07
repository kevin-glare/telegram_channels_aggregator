from telethon import TelegramClient, events, types
import json

with open('config.json') as json_file:
    config = json.load(json_file)
    client = TelegramClient(config['my_channel'], config['api_id'], config['api_hash'])


@client.on(events.NewMessage(chats=config['channel_ids'])) 
async def _(event):
    if isinstance(event.original_update, types.UpdateNewChannelMessage): await client.send_message(config['my_channel'], event.message)


if __name__ == '__main__':
    with client.start(config['mobile_number']):
        print('Press Ctrl+C to stop this')
        client.run_until_disconnected()
