import time
from pytube import YouTube
from pytube.cli  import on_progress
import win32clipboard


win32clipboard.OpenClipboard()
link = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()



yt=YouTube(link, on_progress_callback=on_progress)


x= yt.streams.get_highest_resolution()

x.download()
time.sleep(5)
print("\n")
print("Processo concluido! aperte Enter para sair!")
ab=input() 

