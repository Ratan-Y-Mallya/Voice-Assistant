import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wisMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
         speak("good evening!")
    speak("I am jarvis sir,How can I help you")


def takecommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening....")
          r.pause_threshold = 1
          audio =r.listen(source)

     try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
     except Exception as e:
          #
          # print(e)
          print("say that again please....")
          return "None"
     return query       
if __name__=="__main__":
      wisMe()
      while True:
        query = takecommand().lower()

        if 'wikipedia' in query :
            speak('searching wikipidia....')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
        elif 'open google' in query:
            webbrowser.open("google.com")        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'the time' in query:
            starttime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {starttime}")
        elif 'open code' in query:
            codepath= "C:\\Users\\ymrat\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"

            os.startfile(codepath)
           
