#INSTALL pytubefix FIRST (The same way you installed flet)
#FOR MAC: Open the terminal and run: pip3 install pytubefix
#FOR WINDOWS open your cmd and run: pip install pytubefix
#Yes, this code is from chat gpt but I have done this before but pytube was not working lol
from pytubefix import YouTube
import os
 
def download_audio(url, output_folder=r"your\folder\path\here"):
 
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    print(f"Downloading: {yt.title}")
   
    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)
   
    # Download audio file
    audio_file = audio_stream.download(output_path=output_folder)
   
    # Convert to MP3
    base, ext = os.path.splitext(audio_file)
    mp3_file = base + ".mp3"
    os.rename(audio_file, mp3_file)
   
    print(f"Downloaded and converted to MP3: {mp3_file}")
 
# Example usage
video_url = input("Enter YouTube URL: ")
download_audio(video_url)

#danza kuduro, every breath you take,everybody wants to rule the world, everywhere, gangnam  style, get lucky, golden hour, last friday night, let the light in, levitating, like a prayer, sweaterweather