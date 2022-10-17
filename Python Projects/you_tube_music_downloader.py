'''
Download your favourite music and audio from YouTube in mp3 format.
To run:
python YouTubeMusicDownloader.py <YouTube Link> <Folder Path to save downloaded file in single quotes>
Example:
$ python YouTubeMusicDownloader.py https://www.youtube.com/watch?v=8jQ7Jyb-j8A 'D:\Audio\Downloads'
'''
from pytube import YouTube 
import sys
import os
n = len(sys.argv)
if n != 3:
    print('Error check your command line arguments')
    sys.exit(-1)
if 'https://www.youtube.com/' not in str(sys.argv[1]) and 'https://youtu.be/' not in str(sys.argv[1]):
    print('Enter a valid YouTube link')
    sys.exit(-1)

print('Downloading audio from YouTube Link...')
video = YouTube(sys.argv[1])
SAVE_PATH = sys.argv[2]
audio = video.streams.filter(subtype='mp4').filter(only_audio=True)
out_file = audio[0].download(SAVE_PATH)

print('Converting MP4 file to MP3 audio file...')
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(f'Conversion done. Find your downloaded file at path -> {new_file} and enjoy!')
