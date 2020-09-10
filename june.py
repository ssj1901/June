import pyttsx3
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os
import smtplib
from time import sleep
import datetime
import pywhatkit as kit

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
june = pyttsx3.init('sapi5')
voices = june.getProperty('voices')
june.setProperty('voice',voices[1].id)
june.setProperty('rate',160)
def speak(audio):
    june.say(audio)
    june.runAndWait()

def intro():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time <12:
        speak("Good Morning ")
    elif time>=12 and time <16:
        speak("Good afternoon ")
    else:
        speak("Good evening ")               
    
    
    

def recog_Command():
    r = sr.Recognizer()
    with sr.Microphone() as audio:
         print("Listening...")
         r.pause_threshold = 0.8
         text = r.listen(audio)
         try:
            recognized_text = r.recognize_google(text,language='en-in')
            print("User: {}".format(recognized_text))
         except sr.UnknownValueError:
            print("value is unknown")
            return "none"
         except sr.RequestError as e:
            print("could not process {}").format(e)
            return "none" 
         return recognized_text
if __name__ == "__main__":
    x=1 
    intro()
    while True:
        speak("How may i assist you")
        text = recog_Command().lower()
        if 'wikipedia' in text or ('search' in text and 'wikipedia' in text):
            speak("Searching in Wiki")
            text = text.replace("wikipedia","")
            result = wikipedia.summary(text,sentences=3)
            print("result found")
            speak("According to Wikipedia")
            speak(result)
        elif 'open youtube' in text:
            webbrowser.get('chrome').open("youtube.com")
        elif 'open stackoverflow' in text:
            webbrowser.open("stackoverflow.com")
        elif 'open google' in text:
            webbrowser.get('chrome').open("google.com")   
        elif 'open facebook' in text:
            webbrowser.get('chrome').open("facebook.com")   
        elif 'open amazon' in text:
            webbrowser.get('chrome').open("amazon.com")   
        elif 'open twitter' in text:
            webbrowser.get('chrome').open("twitter.com")               
        elif 'the time' in text:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Well, the time is {current_time}")   
        elif 'search' in text:
            text=text.replace("search","")
            if 'for me' in text:
                text=text.replace("for me","")
            kit.search(text)    
        elif 'play' in text:
            text=text.replace("play","")
            if 'youtube' in text:
                 text=text.replace("youtube","")
            kit.playonyt(text)         
        elif 'stop' in text:
            break

        sleep(5)

        
      