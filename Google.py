import pywhatkit 
import wikipedia 
import pyttsx3

def Speak(Audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    print(Audio)
    engine.say(Audio)
    engine.runAndWait()

def System():
    Search = input("Enter your Quary: ")
    pywhatkit.search(Search)
    data = wikipedia.summary(Search,3)
    Speak(data)

while True:
     System()    