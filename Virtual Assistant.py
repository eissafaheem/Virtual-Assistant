import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import random
import time
import webbrowser
from array import*
import pyautogui
import os
import string


#AGGIGNING VOICE TO ASSISTANTs


engine=pyttsx3.init('sapi5')                                                #pyttsx3 converts entered speech into text 
voices=engine.getProperty('voices')                                         #sapi5 provides pyttsx with 2 voices male and female
#print(voices)                                                              #init provides engine instance for speech synthesis

engine.setProperty('voice',voices[1].id)
#print(voices[1].id)




#FUNCTION TO SPEAK

def speak(audio):
    engine.say(audio)                                                       #say provides input text to be spoken #audio is return type for speak function say also pass it as argument
    engine.runAndWait()                                                     #runandwait processes the voice commands

def wishMe():
    hour=int(datetime.datetime.now().hour)                                  #this function is from datetime library it tells curren time 
    if hour>=0 and hour<12:                                                 #if elif and else greet according to time and invoking speak function each time
        speak("Good Morhning sir")
        
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    
    else:
        speak("Good Evening sir")

    speak("David at your service.")




#FUNCTION FOR RECOGNISING SPEECH AND CONVERTING TO TEXT


def takeCommand():

    r = sr.Recognizer()                                                                          #creating recogniser class(predefined) instance: object(r) for recogniser class
    with sr.Microphone() as source:                                                             #using microphone as input this function is defined in speech recognition
        print("Listning....")
        r.pause_threshold=1                                                                     #set up threshold for holding up between gaps
        audio = r.listen(source)                                                                #it listens from source and extracts it to audio

    try:
        print("Recognising....")
        query=r.recognize_google(audio, language='en-in')                                      #recognising speech using google speech recogniser and storing it into query(variable)
        print("User Said: ",query)
    
    except Exception as e:                                                                     #if not understood
        print(e)
        print("Sir can you please Say that again?")
        speak("Sir can you please Say that again?")
        return "None"
    return query

if __name__ == "__main__":

    wishMe()
    #FUNCTION CONATAINING CONDITIONAL STATEMENTS WHEN QUERY CONTAINS SPECIFIC WORDS
    while True:
        query=takeCommand().lower()
        #searching results from wikipedia
        if 'what is 'in query:
            speak("According to Wikipedia")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        
        #opening youtube
        elif 'youtube'in query:
            webbrowser.open("youtube.com")

        #opening google
        elif 'google' in query:
            webbrowser.open("google.com")

        #narrating time
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        #asking assistant "how are you"
        elif 'how are you' in query:
            how_are_you = ['I am totally fine Sir. Thanks for your concern.','The best I can be. Assuming you’re at your best too sir.','Going great sir. Hope this status quo persists for rest of the day','I’m pretty standard right now. How do you do Sir?','Happy and content, thank you sir','I am blessed sir','Way better than I deserve Sir','Different day, same existence Sir']
            k=random.choice(how_are_you)
            print(k)
            speak(k)
        
        #asking assistant tell me about yourself
        elif 'tell me about yourself' in query:
            about="I am a basic Artificially Intelligent bot, developed by Mr. Eissa M Faheem on 26th May 2021. I drint no food and breathe no air, i can be a good entertaining object, you may try it."
            print(about)
            speak(about)

        #when we want to make a video call
        elif 'whatsapp video call' in query:
            os.startfile("C:\\Users\\eissa\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp")
            time.sleep(5)
            pyautogui.click(294,139)
            vs="PLease tell whom do you want to video call?"
            print(vs)
            speak(vs)
            cname=takeCommand()
            cname=cname.replace(" ","")
            cname=cname.replace("-","")
            pyautogui.typewrite(cname)
            time.sleep(2)
            pyautogui.click(138,297)
            vc="Do you want to make video call to ",cname
            print(vc)
            speak(vc)
            cancel=takeCommand()
            
            if 'cancel' in cancel:
                vcc="Video call cancelling request successfull!"
                print(vcc)
                speak(vcc)
                continue
            else:
                pyautogui.click(1658, 65)

        elif 'type' in query:
            speak('say the message')
            time.sleep(2)
            typ=takeCommand()
            while(typ!='exit'):
                pyautogui.typewrite(typ)
                pyautogui.typewrite(" ")
                typ=takeCommand()
            
        #if user want to compose a whatsapp message
        elif 'whatsapp message' in query:
            w="Opening whatsapp in a few moments."
            print(w)
            speak(w)
            os.startfile("C:\\Users\\eissa\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp")
            time.sleep(5)
            pyautogui.click(199,130)
            q1="Sir please tell to whom this message is to be send?"
            print(q1)
            speak(q1)
            cname=takeCommand()
            sm="Sending message to ",cname 
            print(sm)
            speak(sm)
            con=takeCommand()
            pyautogui.typewrite(cname)
            time.sleep(2)
            speak("are you Confirm?")

            if 'cancel'in con:
                cancelling="Cancelling message request successfull"
                print(cancelling)
                speak(cancelling)
                continue
            
            else:
                pyautogui.click(166, 308)
                q2="Sir please tell the message."
                print(q2)
                speak(q2)
                message=takeCommand()
                time.sleep(2)
                pyautogui.typewrite(message)
                pyautogui.typewrite("\n")
                ms="Message sent."
                print(ms)
                speak(ms)

        #if user says bye
        elif "bye" in query:
            bye = "Hope i was fortunate enough to serve you to the best, thank you sir. David Shutting down"
            print(bye)
            speak(bye )
            exit()
           
       

