import pydub
from pydub import AudioSegment
from os import path
import speech_recognition as sr
from pytube import YouTube
import os


def yt_save(link):
    yt = YouTube(str(input("Enter URL of youtube video: \n ")))
    video = yt.streams.filter(only_audio=True).first()
    print("Enter the destination address (leave blank to save in current directory)")
    destination = str(input(" ")) or '.'
    out_file = video.download(output_path=".")
    base, ext = os.path.splitext(out_file)
    name = (yt.title.split())[0]
    new_file = name + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")
