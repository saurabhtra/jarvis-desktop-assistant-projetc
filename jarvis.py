import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import smtplib

from wikipedia.wikipedia import search
engine=pyttsx3.init('sapi5') #initaling engine wiht sapi5 object
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty("rate")
engine.setProperty('rate',150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning !")
    elif hour>=12 and hour<16:
        speak("Good Afternoon! ")
    else :
        speak("Good Evening !")
    speak("hi I am Jarvis , How may I help you sir?") 

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('saurabhtra1997@gmail.com','Itsme@1234')
    server.sendmail('saurabhtra1997@gmail.com',to, content)
    server.close()

def take_command():#take input from microphone and returns string
    r= sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold=0.79
        audio=r.listen(source)
    try:
        print("Recognition...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception :
        print("Say that again please...")
        return "None"
    return query
       
    
if __name__=="__main__":
    wishMe()
while True:
    query = take_command().lower()
    #Logic for executing command
    if 'wikipedia' in query:
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2) 
        speak("According to wikipedia")
        speak(result)
    elif 'open youtube' in query:
       webbrowser.open('youtube')
    elif 'email' in query:
        try:
            speak('what should i say?')
            content = take_command()
            to = 'saurabhtra1997@gmail.com'
            sendEmail(to,content)
            speak('done sir!')
        except Exception as e:
            print(e)
            speak('sorry sir')
    elif 'time' in query:
        strftime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir time is {strftime}")

    elif 'exit' in query:
        break
