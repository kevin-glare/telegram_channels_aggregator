## Information

A telegram posts aggregator, written in python 3.

 1. First, clone the repository:\
`git clone git@github.com:kgoryachev/telegram_channels_aggregator.git`

 2. Change directory to telegram_channels_aggregator:\
 `cd telegram_channels_aggregator`
 
 3. Install the requirements:\
 `pip install -r requirements.txt`
 
 4. Initialize config config.json:\
    `mobile_number` - mobile number(with telegram account)\
    `api_id и api_hash` - api_id и api_hash from https://my.telegram.org, under API Development\
    `my_channel` - link to your channel without _@_  and  https://t.me/ \
    `channel_ids` - ids channels for collecting posts(you must be subscribed to these channels)\
    `change_links` - search telegram link(@channel) in post and replace by your channel\
    `check_bad_words` - dont send post if it contains is a stop word
 
 5. Start:\
 `python3 channels_agregator.py`
