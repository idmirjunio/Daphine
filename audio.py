
import time
from importlib.resources import path
from re import A
from turtle import title
from pytube import YouTube, streams
from pytube.cli  import on_progress
import win32clipboard
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

win32clipboard.OpenClipboard()
link = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()



yt=YouTube(link, on_progress_callback=on_progress)


x= yt.streams.get_highest_resolution()

x.download()
path=os.getcwd()
lista =os.listdir(path)

for a in lista:
    boo=a.endswith(".mp4")
    if boo is True:title_video=a
title_audio=title_video.strip(".mp4")

video = VideoFileClip(title_video)

video.audio.write_audiofile(title_audio+".mp3")
video.close()
os.remove(title_video)
ab=input("Processo concluido")
time.sleep(5)   
