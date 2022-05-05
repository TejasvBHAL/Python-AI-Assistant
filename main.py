from fileinput import close
import pyttsx3
from datetime import datetime
from decouple import config
import speech_recognition as sr
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import os
import subprocess as sp
from random import choice
from pprint import pprint
paths = {
    'notepad': "C:\\Windows\\Notepad.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]


USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190 )
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def greet_user():
    hour = datetime.now().hour
    
    if hour >= 6 and hour < 12:
        speak(f"Good morning {USERNAME}")
    elif hour >=12 and hour < 16:
        speak(f"Good afternoon {USERNAME}")
    elif hour >= 16 and hour < 21:
        speak(f"Good Evening {USERNAME}") 
    elif hour >= 21 and hour < 24:
        speak(f"Good Night {USERNAME}")
    speak(f"I am {BOTNAME}. How may i assist you?")
    
                      

def user_input():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')    
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if  'exit' in query:
            speak(f"Hey {USERNAME}, I am Soul , Initializing program")
        
        else:
            hour = datetime.now().hour
            if hour >=21 and hour < 6:
                speak("Good Night {Tejasv}")
            else:
                speak('Have a good day sir')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = None
    return  query


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)
    
def search_on_google(query):
        kit.search(query)  
        
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
    


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']  

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
def open_notepad():
     os.startfile(paths['notepad'])
     
 
        
def open_discord():
    os.startfile(paths['discord'])    
    
def open_cmd(): 
    os.system('start cmd')    
    
def open_calculator(): 
    os.startfile(paths['calculator'])       




if __name__ == '__main__':
    greet_user()
    while True:
        query = user_input().lower()
        
        if 'open notepad' in query:
            open_notepad()
            
        elif 'open_discord' in query:
            open_discord()
        elif 'open command prompt' in query or 'open cmd' in query:
                open_cmd()
        elif 'open camera' in query:
            open_camera()
        elif 'open calculator' in query:
            open_calculator()
        
        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = user_input().lower()
            play_on_youtube(video)
        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = user_input().lower()
            search_on_google(query)
        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
        
        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)
        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)
        
        
               
            
            
            
            
                         
            
