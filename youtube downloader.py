from sys import argv
from pytubefix import YouTube
import shutil
import os

from watchdog.utils.patterns import filter_paths

yt = YouTube("https://www.youtube.com/watch?v=ZQ9JO0e9468")
location = input("Enter the file path for download to be placed : ")
stream = yt.streams.get_highest_resolution()
file_path = stream.download(output_path=location)
print(f"Download Complete, File Location : {file_path}")


