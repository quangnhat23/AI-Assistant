import speech_recognition
import pyttsx3
from datetime import date
from time import strftime

ear = speech_recognition.Recognizer()
aiSay =pyttsx3.init()
brain = " " 
with speech_recognition.Microphone() as mic:
    print("AshRock: I'm listening")
    audio = ear.listen(mic)

print("AshRock:...")

try:
    you = ear.recognize_google(audio)
except:
    you ="" 
print("you: "+ you)


if you =="":
	brain = " I can't hear you, try again"
elif you =="hello": 
	brain = " Hello Quang"
elif you =="today":
	today= date.today()
    brain = today.strftime("%Y-%m-%d %H:%M:%S")
else:
    brain= " I am fine, thank you" 

print("AshRock:"+ brain)
aiSay.say(brain)
aiSay.runAndWait()