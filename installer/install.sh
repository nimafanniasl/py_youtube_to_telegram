#!/bin/bash

wget https://github.com/nimafanniasl/py_youtube_to_telegram/raw/main/bot.py
dos2unix bot.py

python -m pip install scrapetube colorama python-telegram-bot pytube

mv bot.py ytt
mv ytt /bin
cd /bin
chmod 777 ytt
