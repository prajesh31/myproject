import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good evening!prajesh')

    elif hour>=12 and hour<18:
        speak('Good morning!')

    else:
        speak('Good afternoon! prajesh')

    speak('I am jarvis sir,please tell me how may i help you') 

def takeCommand():
    #It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listning...')
        r.pause_threshold = 1
        r.energy_threshold=300
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        #print(e)
        print('say that again please...')
        return'None'
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kshirsagar.prajesh@gmail.com','Prajesh31')
    server.sendmail('kshirsagar.prajesh@gmail.com',to,content)
    server.close()






if __name__ == "__main__":
   wishme()
   while True:
   #if 1:
        query= takeCommand().lower()

        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query= query.replace('wikipedia','')
            results= wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(results)

        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'google' in query:
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'whatsapp' in query:
            webbrowser.open('whatsapp.com')


        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f'sir, the time is {strTime}')

        elif 'month' in query:
            strTime= datetime.datetime.now().strftime('%B')
            speak(f'sir, the month is {strTime}')

        elif 'year' in query:
            strTime= datetime.datetime.now().strftime('%Y')
            speak(f'sir, the year is {strTime}')

        
        elif 'day' in query:
            strTime= datetime.datetime.now().strftime('%A')
            speak(f'sir, the day is {strTime}')

        elif 'open code' in query:
            codepath= "C:\\Users\\prajesh kshirsagar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        


        elif 'send email to prajesh' in query:
            try:
                speak('what should i say')
                content= takeCommand()
                to = 'kshirsagar.prajesh@gmail.com'
                sendEmail(to,content)
                speak('Email has been sent')

            except Exception as e:
                #print(e)
                speak('sorry email not sent')

        elif 'send message' in query:
            kit.sendwhatmsg('+919425765950','message=takeCommand()',5,57)
            speak('Message has sent')

       

                

        else:
            if 'lol' in query:
                speak('ok!bye my friend ')
                exit()


        

        
            








     


