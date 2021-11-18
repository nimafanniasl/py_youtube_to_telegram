#!/bin/bash

echo "Are you sure you want to uninstall ytt? (y or n): "
read SURE

if [ $SURE = "y" ]
then
    rm -f /bin/ytt
    echo "If this App have any problems, please report here: https://github.com/nimafanniasl/py_youtube_to_telegram/issues/new"
    sleep 1
    echo "Uninstalled successfully!"
    xdg-open https://github.com/nimafanniasl/py_youtube_to_telegram/issues/new
    else
        echo "OK"
fi
