import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from email.message import EmailMessage
import pywhatkit as kit
import requests
from win10toast import ToastNotifier

# Initialize the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Please say that again...")
        return "None"
    except sr.RequestError:
        print("Request failed; check your network connection.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"
    return query.lower()

def search_wikipedia(query):
    speak('Searching on Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def open_website(url):
    webbrowser.open(url)

def play_music():
    music_dir = 'D:\\songs'
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
    else:
        speak("No songs found in the directory.")

def sendEmail(to, content):
    try:
        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = 'Your Subject'
        msg['From'] = 'Pankaj.baraiya00000@gmail.com'
        msg['To'] = to

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.send_message(msg)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        speak("Sorry, I am not able to send this email")


def send_whatsapp_message(number, message):
    try:
        kit.sendwhatmsg_instantly(f"+{number}", message)
        speak("Message has been sent!")
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")
        speak("Sorry, I am not able to send this WhatsApp message")

def open_application(app_name):
    try:
        if app_name == "command prompt":
            os.system("start cmd")
        elif app_name == "notepad":
            os.system("start notepad")
        elif app_name == "spotify":
            codePath = "C:\\Users\\Pankaj Baraiya\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
        else:
            speak("Application not recognized.")
    except Exception as e:
        print(f"Failed to open application: {e}")
        speak("Sorry, I am not able to open this application")


def set_reminder(title, message):
    try:
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=10)
        speak("Reminder has been set!")
    except Exception as e:
        print(f"Failed to set reminder: {e}")
        speak("Sorry, I am not able to set the reminder")

def basic_conversation(query):
    if 'how are you' in query:
        speak("I am fine, thank you. How are you?")
        
    elif 'your name' in query:
        speak("I am Jarvis, your personal assistant.")
        
    elif 'who created you' in query:
        speak("I was created by a Pankaj under guidance of ashok sir.")
        
    else:
        speak("I am sorry, I don't know how to respond to that.")
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            search_wikipedia(query)

        elif 'open youtube' in query:
            open_website("youtube.com")

        elif 'open google' in query:
            open_website("google.com")

        elif 'open stackoverflow' in query:
            open_website("stackoverflow.com")

        elif 'play music' in query:
            play_music()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open spotify' in query:
            codePath = "C:\\Users\\Pankaj Baraiya\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)

        elif 'email to Pankaj Baraiya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Pankaj.baraiya00000@gmail.com"
                sendEmail(to, content)
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I am not able to send this email")

        elif 'send whatsapp message' in query:
            try:
                speak("To which number should I send the message?")
                number = takeCommand()
                speak("What is the message?")
                message = takeCommand()
                send_whatsapp_message(number, message)
            except Exception as e:
                print(f"Error: {e}")
                speak("Sorry, I am not able to send this WhatsApp message")

        elif 'open command prompt' in query:
            open_application("command prompt")

        elif 'open notepad' in query:
            open_application("notepad")


        elif 'set reminder' in query:
            speak("What is the title of the reminder?")
            title = takeCommand()
            speak("What is the message?")
            message = takeCommand()
            set_reminder(title, message)

        elif 'how are you' in query or 'your name' in query or 'who created you' in query:
            basic_conversation(query)

