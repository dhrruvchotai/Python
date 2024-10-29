import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()  # Initialize text-to-speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(f"Processing command: {c}")

    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

if __name__ == "__main__":
    speak("Initializing Friday....")
    r = sr.Recognizer()
    #for backg noice
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True

    while True:


        try:
            # Listen for the wake word "Luna"
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening for 'Friday'...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            command = r.recognize_google(audio).lower()

            if "friday" in command:
                speak("Yes, how can I help you?")
                
                # Listen for the actual command
                with sr.Microphone() as source:
                    print("Friday Active... Listening for your command.")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio).lower()

                    # Process the command
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Request error; check your internet connection: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
