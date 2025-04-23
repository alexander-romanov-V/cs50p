"""Lecture 9.19 - Etc: say something"""

# pip install pyttsx3

import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
