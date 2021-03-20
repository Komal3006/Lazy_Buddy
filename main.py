import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init()
engine.setProperty("rate", 160)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning")
    else:
        speak("Good evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio = r.listen(source)

    try :
        speak("understood...")
        query = r.recognize_google(audio, language='en-in')
        print("User said : ", query) 

    except Exception:
        speak("Say again")
        return "None" 
    return query       


if  __name__=="__main__" :
    speak("Hello")
    wishMe() 
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wiki")
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")    
                 
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com/")

        elif 'github' in query:
            webbrowser.open("github.com")    

        elif 'leetcode' in query:
            webbrowser.open("leetcode.com")

        elif 'codechef' in query:
            webbrowser.open("codechef.com")

        elif 'codeforces' in query:
            webbrowser.open("codeforces.com")

        elif 'netflix' in query:
            webbrowser.open("netflix.com")

        elif 'facebook' in query:
            webbrowser.open("facebook.com")

        elif 'instagram' in query:
            webbrowser.open("instagram.com")                                 




