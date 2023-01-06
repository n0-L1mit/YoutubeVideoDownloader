from pytube import YouTube
from pytube.cli import on_progress

def Download(link):
    youtubeLink = YouTube(link, on_progress_callback=on_progress) # 'on_progress_callback' for display progress bar
    youtubeObject = youtubeLink.streams.get_highest_resolution()
    
    try:
        youtubeObject.download()
    except:
        print("There has been an error in downloading your youtube video")
    print("\nThe download was successful\n")
    
link = input("URL:\n")
Download(link)