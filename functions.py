import re

def check_bad_words(text, bad_words):
    lower = text.lower()
    for word in bad_words:
        if word in lower:
            return ''
    return text


def change_links(text, my_channel):
    return re.sub('@\S+', '@' + my_channel, text)

def find_channel(channel_id, channels):
    for channel in channels:
        if channel_id in channels[channel]:
            return channel
    return False


def get_channel_ids(channels):
    ids = []
    for channel in channels:
        ids += channels[channel]
    return ids