import speech_recognition as sr
import webbrowser
import pyttsx3

r = sr.Recognizer() #Initialized recognizer obj which recognizes if you speak something. 
engine = pyttsx3.init()  #Initialized text to speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

if( __name__ == "__main__"):

    speak("Initializing Luna....")

    while True:

        #Listen for the wake word "Pyra"
        print("Recognizing...")

        try:
            # obtain audio from the microphone
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=3)

            command = r.recognize_google(audio) # recognize speech using Google.
            print(command) 
            speak(command)
            if(command.lower() == "luna"):
                speak("Yes boss")

        except Exception as e:
            print(f"Error...{format(e)}.")
        
        #9:44:47