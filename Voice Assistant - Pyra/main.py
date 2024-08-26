import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer() #Initialized recognizer obj which recognizes if you speak something.
engine = pyttsx3.init()  #Initialized text to speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

if( __name__ == "__main__"):

    speak("Initializing Pyra....")

    while True:

        #Listen for the wake word "Pyra"
        # obtain audio from the microphone

        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source)

        # recognize speech using Google
        print("Recognizing...")
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print("Google error; {0}".format(e))