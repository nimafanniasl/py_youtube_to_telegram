import scrapetube
import telegram
from pytube import YouTube
import colorama
from time import sleep
import os


YouTube_channel_id = input(colorama.Fore.GREEN + "Enter Youtube channel ID: ")
bot_token = input(colorama.Style.RESET_ALL + colorama.Fore.RED +"Enter Your Telegram BOT Token: ")
channel_or_group_or_chat = input(colorama.Style.RESET_ALL + colorama.Fore.GREEN + "Do you want to sent posts to a chat or a group or channel? (group or channel or chat): ")
if channel_or_group_or_chat == "chat":
    bot_chatID = input(colorama.Style.RESET_ALL + colorama.Fore.GREEN + "Enter Chat ID: ")
elif channel_or_group_or_chat == "group" or channel_or_group_or_chat == "channel":
    print(colorama.Style.RESET_ALL + colorama.Fore.RED + "first, please make your BOT Admin in Your channel or group.")
    bot_chatID = input(colorama.Style.RESET_ALL + colorama.Fore.GREEN + "Now Enter Your Channel or group ID with @: ")

bot = telegram.Bot(token=f'{bot_token}')
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
if channel_or_group_or_chat == "group" or channel_or_group_or_chat == "channel":
    enter_Channel_ID = input("Do you want to send Your channel id in end of posts? (yes or no): ")
else:
    enter_Channel_ID = None

for i in list(range(len(videos))):
    yt = YouTube(videos[i])
    print(colorama.Fore.GREEN + "[↓]" + colorama.Style.RESET_ALL + " " + colorama.Fore.RED + f"{yt.title}" + colorama.Style.RESET_ALL + " " + colorama.Fore.GREEN + "Downloading...")
    ys = yt.streams.get_highest_resolution()
    ys.download()
    if enter_Channel_ID == "yes":
        upload_video(str(yt.title), str(yt.description),True)
        print(colorama.Fore.GREEN + "[+]" + colorama.Style.RESET_ALL + " " + colorama.Fore.RED + f"{yt.title}" + colorama.Style.RESET_ALL + " " + colorama.Fore.GREEN + "Uploaded Completely!")
    elif enter_Channel_ID == "no" or enter_Channel_ID == None:
        upload_video(str(yt.title), str(yt.description),False)
        print(colorama.Fore.GREEN + "[+]" + colorama.Style.RESET_ALL + " " + colorama.Fore.RED + f"{yt.title}" + colorama.Style.RESET_ALL + " " + colorama.Fore.GREEN + "Uploaded Completely!")
input()
