from os import path
from pydub import AudioSegment

sound = AudioSegment.from_mp3("How.mp3")
sound.export("transcript.wav", format="wav")
