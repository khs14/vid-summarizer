import speech_recognition as sr
import pydub
r = sr.Recognizer()


def get_txt(file_name):
    with sr.AudioFile(file_name) as source:
        audio_text = r.record(source)
    text = r.recognize_google(audio_text)
    return text
