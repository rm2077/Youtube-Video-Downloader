import os
from pytube import YouTube

output_path = 'Enter File Name'
while True:
  url = input("Enter the youtube link you want to download: ")

  if "youtu.be" in url and "https://" in url:
        newurl = str(url)
        break
  else:
    print("Please try again...")


try:
  if not os.path.exists(output_path):
    os.makedirs(output_path)
  yt = YouTube(newurl)
  video = yt.streams.filter(progressive=True, file_extension='mp4').first()
  video.download(output_path=output_path)
  print(f'Video is downloaded to {output_path}')
except Exception as e:
  print(f'Error Occured: {e}')