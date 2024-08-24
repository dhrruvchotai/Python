import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer() #Initialized recognizer obj which recognizes if you speak something.
engine = pyttsx3.init()  #Initialized text to speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

if( __name__ == "__main__"):
    speak("Initializing Pyra....")