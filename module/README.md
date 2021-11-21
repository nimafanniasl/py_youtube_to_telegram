# ytt module For Python

for install this module, Run This command:
```
pip install ytt
```
-----------------------------------------
 
for import:
 
```
from ytt import ytt
```

-----------------------------

# Usage:

```
start_all(YouTube_channel_id,telegram_bot_token,bot_chatID,send_channel_or_group_id=None):
  Using this function in your Python application, you can download all the videos of a YouTube channel and transfer them to Telegram.
    YouTube_channel_id (str): ID of Youtube Channel You want To send All videos of This channel to Telegram,
    telegram_bot_token (str): Your Telegram Bot Token (If you have not made a telegram bot, create a bot through this bot in Telegram: @BotFather),
    bot_chatID (str): ChatID of your Telegram Channel, Group or Chat,
    send_channel_or_group_id (bool): If You want to append Your channel or Group ID to the end of post, You can send True, But if you Do not want to Use it, leave it empty!
```
----------------------------------------

```
Download_only(YouTube_channel_id):
    Download All videos Of a Youtube Channel Only.
      YouTube_channel_id (str): ID of YouTube channel
```
--------------------------------------

```
upload_downloaded_videos(telegram_bot_token,bot_chatID,send_channel_or_group_id=None):
  Upload Downloaded videos with Download_only Function to Telegram
    Usage:
      telegram_bot_token (str): Your Telegram Bot Token (If you have not made a telegram bot, create a bot through this bot in Telegram: @BotFather),
      bot_chatID (str): ChatID of your Telegram Channel, Group or Chat,
      send_channel_or_group_id (bool): If You want to append Your channel or Group ID to the end of post, You can send True, But if you Do not want to Use it, leave it empty!
```
