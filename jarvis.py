import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import smtplib



engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') 
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):

   engine.say(audio) 

   engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
       speak("Good Morning! sir")
   elif hour>=12 and hour<18:
       speak("Good Afternoon! sir")
   else: 
       speak("Good Evening! sir") 

# speak("I'm Jarvis Sir, How may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
    return query
 

 
if __name__ == "__main__":
    wishMe()
    speak("I'm Jarvis, How may i help you")
    while True:
        # if 1:
        query = takeCommand().lower() 

        # Logic
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening on youtube")
            webbrowser.open("youtube.com")
            #webbrowser.open("youtube.com/results?sp=mAEB&search_query="+query)

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open google' in query:
            webbrowser.open("stackoverflow.com")        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vscode' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    
        
        elif 'Sent email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "SwayamSoni.1905@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry bhai. I am not able to send this email")    

        elif 'open mobile camera' in query:
            import urllib.request
            import cv2 #pip install opencv-python
            import numpy as np #pip install numpy
            import time
            URL = "http://192.168.43.1:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray (urllib.request.urlopen(URL).read()),dtype-np.uint8)
                img = cv2.imdecode(img_arr,-1) 
                cv2. imshow('IPWebcam', img)
                q=cv2. waitKey(1)
                if q==ord("q"): 
                    break;

            cv2.destroyAllWindows()
    
        elif "activate Search Anything" in query:  # import pywikihow
        
            speak("Search Anything is activated please tell me what you want to know")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def pdf_reader():
    book=open('py3.pdf','rb') #rb = readBinary
    pdfReader = PyPDF2.PdfFileReader (book) #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number i have to read")
    pg= int (input ("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText ()
    speak(text)