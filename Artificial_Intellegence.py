"""
AUTHOR : HAIDER ALI 
DATE   : JANUARY 16 2021
PURPOSE: TO CREATE A AI VOICE ASSISTANT IN PYTHON ..
"""


import pyttsx3
import datetime
import speech_recognition as sr  # pip instal speechRecognition
import wikipedia
import webbrowser
import os
import smtplib

# email_content = {'haider':'007harryjutt@gmail.com','ali':'007razajutt@gmail.com'}

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """
    THIS FUNCTION WISH THE USER DEPEND ON TIME
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        print("GOOD MORNING ! ")
        speak("Good Morning")
    elif hour >= 13 and hour <= 17:
        print("GOOD AFTERNOON !")
        speak("Good Afternoon")
    else:
        print("GOOD EVENING !")
        speak("Good Evening")
    speak("I am David Sir Please tell me how may i help you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said : {query}\n")
    except Exception as e:
        print("Say That Again Please ? ")
        # print(e)
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    # takeCommand()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            try:
                print("David : Searching Wikipedia ...\n")
                speak("Searching Wikipedia")
                query = query.replace('wikipedia','')
                results = wikipedia.summary(query,sentences=1)
                speak("Alright ... ")
                print("David : Acording To Wikipedia\n")
                speak("Acording To Wikipedia ...")
                print(results,'\n')
                speak(results)
            except Exception as e:
                print("David : No Results Found !!!")
                speak("No Results Found")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack over flow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = r"F:\harry_programmes\Projects\David or Jarvis Projects AI\Fav songs"
            songs = os.listdir(music_dir)
            # print(time)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(time)
        elif 'open code' in query:
            code_path="C:\\Users\\N.S COMPUTERS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)


        # elif "send email" in query:
        #     for name,adress in email_content.keys():
        #         if name in query:
        #             try:
        #                 print("David : What Should I Say ?\n")
        #                 speak("What Should I say")
        #                 content = takeCommand()
        #                 to = f"{adress}"
        #                 sendEmail(to,content)
        #                 print("Email Has Been Sent !\n")
        #                 speak("Email has been sent ")
        #             except Exception as e:
        #                 print(f"David : I am not able to send this e-mail")
        #                 speak("I am not able to send this email")


        elif 'what is your name ?' in query or 'author of this softwate' in query:
            speak("I Am Assistant Of Haider and My name is David")
            print(f"David : I Am Assistant Of Haider and My name is David \n")
        elif 'haider calculator' in query:
            cal_path=r"F:\harry_programmes\Projects\Calculator\build\exe.win-amd64-3.9\Calculator.exe"
            os.startfile(cal_path)
        elif "what you can do" in query:
            command = f"1 . Wikipedia\t2 . Youtube\t3 . Google\t4 . VS Code\t5 . Stackoverflow\n6 . Time\t7 . Calcultor Haider\t8 . Play Music\t9 . Email Send\n"
            
            speak("I Command On This Function For User ")
            print("I Command On This Function For User ...\n")
            print(command)
            speak(command)
        elif 'quite' in query or 'close' in query or 'stop' in query:
            exit()
        else:
            pass
        # else:
        #     print("I Can Not Able To Solve Your request ...")
        #     speak("I Can not able to solve your request")