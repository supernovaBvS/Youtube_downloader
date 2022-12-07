from pytube import YouTube
from pytube import Playlist
from tqdm import tqdm
from time import sleep
from sys import argv

link = argv[1]
p = Playlist(link)
title = p.title
print("Title: ", p.title)

print("View: ", p.views)

for video in tqdm(p.videos):
    sleep(0.00001)
    yd = video.streams.get_highest_resolution().download('/Users/dev/Desktop/YTfolder')
else:
    print(f'Sussesfully downloaded {title}')