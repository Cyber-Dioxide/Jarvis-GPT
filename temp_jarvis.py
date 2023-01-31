import datetime
import os
import random
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
import wikipedia
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)




def speak(something):
    engine.say(something)
    engine.runAndWait()


def printWithSpeek(msg):
    print(msg)

    speak(msg)


def cmd(str):
    os.system(str)




def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning {user_name}")
    elif hour <= 12 and hour >= 18:
        speak(f"Good Afternoon {user_name}")
    else:
        speak(f"Good Evening {username}")
    printWithSpeek("Iam Jarvis, Tell me how can i help you?")


def speekInput():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        printWithSpeek('\rListening... ')
        rec.pause_threshold = 1
        listen = rec.listen(mic)
    try:
        print("\rRecognizing... ")
        query = rec.recognize_google(listen, language='en-US')
        print(f"Query: {query}")
    except Exception as e:
        printWithSpeek("I was unable to recognize, please say again! ")
        return 'None'
    return query.lower()


def playSong(dir=music_dir):
    music_files = os.listdir(dir)
    total_files = len(music_files) - 1
    index = 0

    os.startfile(dir + music_files[random.randint(index, total_files)])


def exitCheck(output):
    if 'and' in output.split():

        if 'exit' in output.split():
            exit(0)
        return True


def SelectSomething():
    speak('Enter file path to search....')
    file_path = input("Enter: ")
    return file_path


def check_code(url):
    req = requests.get(url)
    if req.status_code == 200:
        return True
    else:
        return False


def showFiles(path):
    files = os.listdir(path)
    for i, file in enumerate(files):
        speak("I found the Following files")

        print(f"[{i}] \t {file}")
    choose = speekInput()
    if choose < len(files):
        os.startfile(files[int(choose)])
    else:
        speak('Index Out Of range, i was unable to start file')


sits_names = ['google', 'github', 'youtube', 'tryhackme', 'instagram', 'spotify', 'facebook', 'duckduckgo'
    , 'amazon', 'ebay', 'stackoverflow']

query_list = ['/results?search_query=', '/search?q=', '/?t=ffab&q=', '/?=']
windows_applications = ['']

c_drice = 'C:\\'
d_drive = 'D:\\'


def main():
    global outputt
    greet()
    while True:

        output = speekInput()

        if 'wikipedia' in output:
            printWithSpeek('Searching Wikipedia...')
            outputt = output.replace('wikipedia', "")
            outputt = outputt.replace('Wikipedia ', "")
            results = wikipedia.summary(outputt, sentences=2)
            printWithSpeek(results)

        elif 'open ' in output:
            outputt = outputt.replace('for', '')
            outputt = outputt.split()
            search_index = outputt.index('open') + 1
            x = outputt[search_index]
            if x in sits_names:

                site = 'https://' + x + '.com'

                if 'search' in outputt:
                    query = outputt.index('search') + 1
                    query = outputt[query:]

                    search = ''
                    for word in query:
                        search += word + '+'
                    printWithSpeek(f'Opening {x} and searching...')
                    for q in query_list:
                        if check_code(site + q + search[0:-1]):
                            webbrowser.open(site + q + search[0:-1])


                else:
                    printWithSpeek(f'Opening {x}')
                    webbrowser.open(site)

            exitCheck(output)

        elif 'play music' in output:
            playSong('C:\\Users\\shauk\\Downloads\\Music\\')
            exitCheck(output)
            exitCheck(output)

        elif output == 'exit':
            speak("GoodBye Saad")
            exit()

        elif 'show files' in output:
            x = SelectSomething()
            showFiles(x)

        elif 'gpt' in output or 'gpt mode' in output:
            

try:
    main()
except Exception as e:
    printWithSpeek(e)
