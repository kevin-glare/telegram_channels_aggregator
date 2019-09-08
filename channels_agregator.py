from telethon import TelegramClient, events, types
import functions as f
import json

with open('config.json') as json_file:
    config = json.load(json_file)
    channels = config['channels']
    channel_ids = f.get_channel_ids(channels)
    client = TelegramClient(config['mobile_number'], config['api_id'], config['api_hash'])


@client.on(events.NewMessage(chats=channel_ids)) 
async def _(event):
    message = event.message
    channel = f.find_channel(int(event.message.to_id.channel_id), channels)

    if config['functions']['check_bad_words']['status']:
        message.raw_text = f.check_bad_words(message.raw_text, config['functions']['check_bad_words']['bad_words'])

    if config['functions']['change_links']['status']:
        message.raw_text = f.change_links(message.raw_text, channel)

    if isinstance(event.original_update, types.UpdateNewChannelMessage): 
        await client.send_message(channel, message)


if __name__ == '__main__':
    with client.start(config['mobile_number']):
        print('Press Ctrl+C to stop this')
        client.run_until_disconnected()
