

import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
from keyboard import press_and_release
from keyboard import press
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" listing......")
        r.pause_threshold = 0.7
        # r.energy_threshold = 120
        # r.dynamic_energy_adjustment_damping = 0.12
        audio = r.listen(source)
    try:
        print(" recognizing ......")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query} \n")
    except Exception as e:
        # print(e)
        print(" say that again please !")
        return "none"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Wishme():
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour <=12:
            speak("Hi good morning !")
        elif hour >= 12 and hour <=18:
            speak("good afternoon")
        else:
            speak("good evening ")
def sendmail(to,content):
    server= smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("asmsnjas8755@gmail.com","dcqpiuaavxdygtpg")
    server.sendmail("asmsnjas8755@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    speak(" this is your new project ")
    Wishme()
    speak(" hey , i am zira , please tell me how i can help you sir")
    while 1:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            speak("according to wikipedia")
            # speak(results)
            print(results)
            speak(results)
        # elif'open youtube' in query:
        #     webbrowser.open("youtube.com")
        # elif 'open flipkart' in query:
        #     webbrowser.open("flipkart.com")
        # elif 'open google' in query:
        #     webbrowser.open("google.com")
        if 'how are you' in query:
            speak('i am fine sir and you')

        if 'open' in query:
            name = str(query.replace("open",""))
            namea = str(name)
            if 'youtube' in name:
                 webbrowser.open("youtube.com")
            elif 'login page' in query:
                webbrowser.open("http://172.11.8.1:8090/httpclient.html")
            elif 'new tab' in query:
                press_and_release('ctrl+t')
            elif 'close tab' in query:
                press_and_release('ctrl+w')
            elif 'new window' in query:
                press_and_release('ctrl+n')
            elif 'history' in query:
                press_and_release('ctrl+h')
            elif 'download' in query:
                press_and_release('ctrl+j')
            elif 'bookmark' in query:
                press_and_release('ctrl+d')
                press('enter')
            elif 'incognito' in query:
                press_and_release('ctrl+Sift+n')
            elif 'switch tab' in query:
                tab = query.replace("switch tab to","")
                bb = f'ctrl+{tab}'
                press_and_release(bb)
            elif 'close tab' in query:
                press_and_release('ctrl+w')

        # elif 'send mail' or 'send e mail' in query:
        #         try:
        #             speak("what i should send ")
        #             content = take_command()
        #             to = take_command()
        #             sendmail(to,content)
        #             speak("email has been send sucessfully")
        #         except  Exception as e:
        #             print(e)
        #             speak(("email has not been send due to some error "))
        else:
            string = name+".com"
            stringA = string.replace(" ","")
            webbrowser.open(stringA)

