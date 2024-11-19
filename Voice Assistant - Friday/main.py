import speech_recognition as sr
import webbrowser
import pyttsx3
# import musicLibrary
import pywhatkit
from datetime import datetime
import pyjokes
import requests
import re
import time




engine = pyttsx3.init()  # Initialize text-to-speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_api_key():
    with open('Apikey.txt', 'r') as file:
        api_key = file.read().strip() 
    return api_key

def generate_image(prompt):
    api_key = get_api_key() 
    print(api_key)
    headers = {"Authorization": f"Bearer {api_key}"}
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        prompt = prompt.replace("create an image of"," ").strip()
        with open(f"{prompt}.png", "wb") as f:
            f.write(response.content)
        print("Image saved as generated_image.png")

    elif response.status_code == 503:
        print(f"Model is loading. Retrying in {response.json()['estimated_time']} seconds...")
        time.sleep(response.json()['estimated_time'] + 5)

    else:
        print("Error:", response.status_code, response.text)

def addTodo(prompt):
    with open("TodoList.txt","a") as f:
        prompt = prompt.replace("add task"," ").strip()
        f.write(f"{prompt} \n")
    print("added task to your todo list.")

def processCommand(c):
    print(f"Processing command: {c}")

    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    # elif c.lower().startswith("play"):
    #     song = c[5:].strip()
    #     link = musicLibrary.music[song]
    #     webbrowser.open(link)

    elif "play" in c.lower():
        song = c.replace("play"," ").strip()
        text = f"playing {song}..."
        speak(text)
        print(text)
        pywhatkit.playonyt(song)

    elif "search" in c.lower():
        command = c.replace("search"," ").strip()
        text = f"searching for the {command}..."
        speak(text)
        print(text)
        pywhatkit.search(command)

    elif "time" in c.lower():
        time = datetime.now().time()
        print(f"current time is {time}")
        speak(time)

    elif "date" in c.lower():
        date = datetime.now().date()
        print(f"current date is {date}")
        speak(date)
    
    elif "joke" in c.lower():
        joke = pyjokes.get_joke()
        print(f"here is your joke : {joke}")
        speak(joke)

    elif "calculate" in c.lower():
        command = c.lower().replace("calculate", "").strip()
        command = command.replace("plus", "+").replace("minus", "-").replace("times", "*").replace("divided by", "/")
        command = command.replace("x", "*") 
        ans = eval(command)
        print(f"Your ans is : {ans}")
        speak(f"your answer is : {ans}")
    
    # elif "print api" in c.lower():
    #     api = get_api_key()
    #     speak("here is your api key = ")
    #     print(api)

    elif "create an image" in c.lower():
        command = c.lower().replace("generate an image"," ").strip()
        generate_image(command)
    
    elif "add task" in c.lower():
        command = c.lower().replace("add todo"," ").strip()
        addTodo(command)
        



if __name__ == "__main__":

    speak("Initializing Friday....")
    r = sr.Recognizer()

    #for backg noice
    r.energy_threshold = 300
    r.dynamic_energy_threshold = True

    while True:


        try:
            # Listen for the wake word "Friday"
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("Listening for 'Friday'...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            command = r.recognize_google(audio).lower()

            if "friday" in command:
                speak("Yes..")
                
                # Listen for the actual command
                with sr.Microphone() as source:
                    print("Friday Active... Listening for your command.")
                    audio = r.listen(source, timeout=7, phrase_time_limit=7)
                    command = r.recognize_google(audio).lower()

                    # Process the command
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Request error; check your internet connection: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

