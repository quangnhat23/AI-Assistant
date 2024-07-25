import speech_recognition
ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("AshRock: I'm listening")
    audio = ear.listen(mic)
try:
    you = ear.recognize_google(audio)
except:
    you ="" 
print("you: "+ you)