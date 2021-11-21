import scrapetube
import telegram
from pytube import YouTube
import os

list_of_all_Downloaded = []

def Download_only(YouTube_channel_id):
    '''Download All videos Of a Youtube Channel Only
        Usage:
            YouTube_channel_id (str): ID of YouTube channel'''
    c_videos = scrapetube.get_channel(YouTube_channel_id)
    videos = list()
    for video in c_videos:
       videos.append(f"https://www.youtube.com/watch?v={str(video['videoId'])}")
    videos.reverse()
    for i in list(range(len(videos))):
        if list_of_all_Downloaded[i] != []: list_of_all_Downloaded[i] = []
        yt = YouTube(videos[i])
        ys = yt.streams.get_highest_resolution()
        ys.download()
        title = str(yt.title())
        discription = str(yt.description)
        list_of_all_Downloaded[i].append(title)
        list_of_all_Downloaded[i].append(discription)

def upload_downloaded_videos(telegram_bot_token,bot_chatID,send_channel_or_group_id=None):
    '''Upload Downloaded videos with Download_only Function to Telegram
        Usage:
            telegram_bot_token (str): Your Telegram Bot Token (If you have not made a telegram bot, create a bot through this bot in Telegram: @BotFather),
            bot_chatID (str): ChatID of your Telegram Channel, Group or Chat,
            send_channel_or_group_id (bool): If You want to append Your channel or Group ID to the end of post, You can send True, But if you Do not want to Use it, leave it empty!
    '''
    bot = telegram.Bot(token=f'{telegram_bot_token}')
    def upload_video(title, desc, temp):
        if temp == True:
            desc = desc + f"\n\n{bot_chatID}"
        else:
            pass
        str = f"{title}.mp4"
        str = str.replace('"','')
        str = str.replace("'","")
        str = str.replace(",","")
        str = str.replace(".","")
        str = str.replace("mp4",".mp4")
        bot.send_video(chat_id=bot_chatID, video=open(fr'{str}', 'rb'),caption=f"{desc}", supports_streaming=True)
        os.remove(str)
        for i in list(range(len(list_of_all_Downloaded))):
            upload_video(list_of_all_Downloaded[i][0],list_of_all_Downloaded[i][1],send_channel_or_group_id)

def start_all(YouTube_channel_id,telegram_bot_token,bot_chatID,send_channel_or_group_id=None):
    '''Using this function in your Python application, you can download all the videos of a YouTube channel and transfer them to Telegram.
        Usage:
            YouTube_channel_id (str): ID of Youtube Channel You want To send All videos of This channel to Telegram,
            telegram_bot_token (str): Your Telegram Bot Token (If you have not made a telegram bot, create a bot through this bot in Telegram: @BotFather),
            bot_chatID (str): ChatID of your Telegram Channel, Group or Chat,
            send_channel_or_group_id (bool): If You want to append Your channel or Group ID to the end of post, You can send True, But if you Do not want to Use it, leave it empty!
    '''
    bot = telegram.Bot(token=f'{telegram_bot_token}')
    c_videos = scrapetube.get_channel(YouTube_channel_id)
    videos = list()
    for video in c_videos:
       videos.append(f"https://www.youtube.com/watch?v={str(video['videoId'])}")
    videos.reverse()
    def upload_video(title, desc , temp):
        if temp == True:
            desc = desc + f"\n\n{bot_chatID}"
        else:
            pass
        str = f"{title}.mp4"
        str = str.replace('"','')
        str = str.replace("'","")
        str = str.replace(",","")
        str = str.replace(".","")
        str = str.replace("mp4",".mp4")
        bot.send_video(chat_id=bot_chatID, video=open(fr'{str}', 'rb'),caption=f"{desc}", supports_streaming=True)
        os.remove(str)
    

    for i in list(range(len(videos))):
        yt = YouTube(videos[i])
        ys = yt.streams.get_highest_resolution()
        ys.download()
        upload_video(str(yt.title), str(yt.description),send_channel_or_group_id)