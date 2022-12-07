from pytube import YouTube
from tqdm import tqdm
from time import sleep
from sys import argv

link = argv[1]
yt = YouTube(link)
title = yt.title
print("Title: ", title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

for i in tqdm(range(0,100),total=100):
    sleep(0.01)
    yd.download('.YTfolder') # change directory before downloading video that you want to put in
else:
    print(f'Sussesfully downloaded {title}')