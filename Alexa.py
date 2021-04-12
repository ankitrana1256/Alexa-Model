import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests
import os
import sys
import random
import keyboard
from selenium import webdriver

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
        
    speak("I AM YOUR DIGITAL ASSISSTANT Alexa , YOU ARE RUNNING FIRST VERSION. WELCOME HUMAN")
    speak("HOW CAN I HELP YOU")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that!...try typing it')
        query = str(input('TYPE YOUR COMMAND HERE: '))
    
    except RequestError:
        print("PLEASE CONNECT TO THE INTERNET")

    
    return query

if __name__ == "__main__": 
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if "who are you" in query:
            speak("I AM Alexa...AND THIS A TEST VERSION OF AN AI MADE BY ANKIT")
            print("I AM Alexa...AND THIS A TEST VERSION OF AN AI MADE BY ANKIT")
            
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" THE TIME IS {strTime}")

        elif "youtube" in query:
            query = query.replace("youtube", "")
            speak("Opening youtube") 
            webbrowser.open('https://www.youtube.com/results?search_query=' + query)

        elif "open google" in query:
            speak("Opening google") 
            webbrowser.open("www.google.com")

        elif "open instagram" in query:
            speak("Opening instagram") 
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            speak("Opening facebook") 
            webbrowser.open("www.facebook.com")

        elif "wikipedia" in query:
            print("Searching...PLEASE WAIT")
            outputs = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(outputs)
            speak(outputs) 

        elif "play music" in query:
            songs = os.listdir("F:\\songs\\New folder")
            d = random.choice(songs)
            print(d)
            os.startfile("F:\\songs\\New folder\\" + d)
            
        elif "visual code" in query: 
            speak("Opening visual code") 
            os.startfile("C:\\Users\\Priyanka Rana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe") 

        elif "bye" in query:
            exit()

        elif "repeat" in query:
            query = query.replace("repeat", "")
            speak(query)

        elif "question" in query:
            speak("what is your question?")
            question = takeCommand()
            browser = webdriver.Chrome()
            browser.implicitly_wait(1)
            browser.maximize_window()
            browser.get('https://www.wolframalpha.com')
            search_bar = browser.find_element_by_xpath("/html/body/div/div/div/div/div/div[1]/section/form/div/div/input")
            search_bar.send_keys(question)
            keyboard.press_and_release('enter')

        else:
            speak("searching on google for " + query)
            say = query.replace(' ', '+')
            webbrowser.open('https://www.google.co.in/search?q=' + query)