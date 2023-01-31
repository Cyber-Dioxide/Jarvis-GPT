import os
import platform
import random
from os import system
import time
import datetime
import json
from files.robot_logos import retro_robo
import ai_jarvis
from files.advice import advise
from files.check_platform import check
import subprocess
from files.banner import banner
from log import log_data
from files.wiki_search import search
from files.number_tracker import location_tracker
import requests
from files.checkWhether import weather
import sys
import pyjokes
import pyttsx3
import speech_recognition as sr
from colorama import Fore
import threading
from files.youtube import youtube

Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.LIGHTWHITE_EX
G = Fore.GREEN
R = Fore.RED

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 150)


with open('config.json' , 'r') as f:
    data = json.loads(f.read())

user_name= data['NAME']
music_dir = data['MUSIC']


def print_msg(logo='+', msg=''):
    print(f'{W}[{C}{logo}{W}] {Y}{msg}')


def cal_date():
    date = datetime.datetime.now().strftime('%H:%M:%S  -  %D')
    print_msg(logo=f'{Y}>', msg=f'{W}' + str(date))


def clear():
    system('cls') if 'Windows' in platform.platform() else system('clear')
    cal_date()


clear()
print(retro_robo())
banner()



log_file = 'logs/log.txt'
dir = music_dir

garbage = ''


def dance_robo(text):
    robo = f"""
{Y}٩{R}({W}-{G}_{W}-̃{R}){Y}۶
"""
    print(robo + f"{C}" + text, end="\r")


def speak(something):
    print(f'{R}({W}+_+{R}) {Y}{something}')
    engine.say(something)
    engine.runAndWait()


def greet():
    speak('Welcome back Mr.Saad')
    speak("Iam Jarvis, Tell me how can i help you?")


def printWithSeak(msg):
    print(msg)
    speak(msg)


def shell(command):
    system(command)


def playSong(d=dir):
    files = os.listdir(d)

    index = random.randint(0, len(files) - 1)

    print(f'Playing {files[index].replace("_", " ")}')
    os.startfile(d + files[index])


def SelectSomething():
    speak('Enter file path to search....')
    file_path = input("Enter: ")
    return file_path


def speakInput():
    print("[+] Listening", end="\r")
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.pause_threshold = 1
        listen = rec.listen(mic)
    try:
        print("[►] Recognizing... ", end='\r')
        query = rec.recognize_google(listen, language='en-IN')
        print(f"Query: {query}")
        query = query.lower()
    except Exception as e:
        # printWithSpeak("I was unable to recognize, please say again! ")
        return 'None'
    return query.lower()


def menu_of_Files(d):
    files = os.listdir(d)
    for i, file in enumerate(files):
        print_msg(logo=str(i), msg=file)
    speak('Select Song')
    index_of_file = int(speakInput().replace('play', "").replace(' ', ''))
    os.startfile(d + files[index_of_file])


accept_commad = ['roger that sir', 'copy that sir', 'on my way sir', 'Won\'t dissapoint you sir']


def type_myself(ckeck):
    if 'i would like to type myself' in ckeck or 'type myself' in ckeck or 'let me type' in ckeck:

        speak('Sure sir...')
        return input('Enter: ')
    else:
        command = random.choice(accept_commad)
        speak(command)
        return False


def checkExit(msg):
    if 'and' in msg.split():
        if 'exit' in msg.split():
            exit(0)
        else:
            pass


def CheckStatus(url, show='status'):
    res = requests.get('http://' + url)
    response_output = {'headers': res.headers, 'history': res.history, 'cookies': res.cookies,
                       'content': res.content, 'text ': res.text, 'status': res.status_code}

    if show in response_output.keys():
        print_msg(logo="+", msg=str(response_output.get(show)))
    else:
        speak('No data found')


sits_names = ['google', 'github', 'youtube', 'tryhackme', 'instagram', 'spotify', 'facebook', 'duckduckgo'
    , 'amazon', 'ebay', 'stackoverflow']

mark_words = ['iam absolutely fine sir, tell me how can i serve you sir.',
              'Better than fantastic would be an understatement sir.'
    , 'Your voice is more bolder than me sir, this gives me power to stay active',
              'I was scanning files for malware infections',
              'Iam absolutely fine, iam glad to hear your voice']


# cal_date()
# greet()

def main():
    global garbage
    while True:
        output = speakInput()
        output.replace('lock that', 'log that').replace('jarvis', "")

        if 'open youtube' in output.lower():
            output = output.replace('open', '')
            # if output.split()[1] in sits_names:
            youtube(output)

        elif 'weather' in output:
            speak('searching')
            if 'of' in output.split():
                index = output.index('of')
                city = output[index:]
                try:
                    garbage = weather(city)
                    printWithSeak(garbage)
                except Exception as e:
                    printWithSeak(e)
            elif 'in' in output.split():
                index = output.index('in')
                city = output[index:]
                try:
                    garbage = weather(city)
                    printWithSeak(garbage)
                except Exception as e:
                    printWithSeak(e)
            else:
                speak('Tell me city name sir')
                city = speakInput()
                try:
                    garbage = weather(city)
                    printWithSeak(garbage)
                except Exception as e:
                    printWithSeak(e)

        elif 'play random song' in output or 'play a random song' in output:
            playSong()

        elif 'play song' in output or 'play a song' in output:
            speak('Playing')
            menu_of_Files(music_dir)

        elif 'show website' in output or 'check website' in output:
            q = output.split().index('website')
            q = output[q + 1]
            speak('Tell me the name of website sir')
            site = speakInput()
            if type_myself(output):
                site = type_myself(output)
            else:
                CheckStatus(site, q)
        elif 'show me date' in output or 'show time' in output or 'tell me time' in output:
            date = datetime.datetime.now().strftime('%H:%M:%S')
            printWithSeak(date)
            day = datetime.datetime.now().strftime('%A')
            printWithSeak(f'Today is {day}')

        elif 'search for' in output or 'how to' in output or 'what the heck' in output:
            output = output.replace('search for', '')
            output = output.replace('how to', '')
            output = output.replace('what the heck is', '')
            garbage = search(output)
            printWithSeak(garbage)

        elif 'take a log' in output or 'log that' in output:
            speak('Logging that sir')
            log_data(data=garbage, log_file=log_file)

        elif 'how are you' in output or 'what\'s up mark' in output:

            speak(random.choice(mark_words))

        elif 'task manager' in output:
            print("opening task manager....")
            speak("opening task manager sir")
            man_path = r'C:\Windows\system32\Taskmgr.exe'
            os.startfile(man_path)

        elif 'shutdown system' in output:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'joke' in output:
            joke = pyjokes.get_joke()
            printWithSeak(joke)

        elif 'track phone number' in output or 'track the number' in output:

            if type_myself(output):
                # speak("Enter Number sir.")
                num = input("Enter Number: ")
                garbage = location_tracker(num)
                printWithSeak(garbage)
            else:
                speak("Tel me the number sir")
                num = speakInput()
                garbage = location_tracker(num)
                printWithSeak(garbage)

        elif 'change music directory' in output or 'change music folder' in output or 'change songs directory' in output or 'change directory' in output:
            speak('changing directory')
            dir = input('Enter > ')
            if os.path.exists(dir):
                speak('Directory changed successfully sir')
            else:
                speak('Path not found sir, there might be an error in future')

        elif 'execute' in output:
            shell('')
        elif 'system status' in output or 'performance status' in output:
            pass
        elif "who are you" in output:
            speak("Iam jarvis, programmed by professor Saad Khan AKA Cyber-Dioxide")

        elif "advice" in output:
            printWithSeak(advise())
        elif 'activate ai mode' in output or 'auto mode' in output or 'advance mode' in output or 'intelligent mode' in output or 'god mode' in output:
            k = True
            speak('Activating God Mode Sir.')
            while k:
                prompt = speakInput()
                if 'exit god mode' in prompt or 'exit advance mode' in prompt:
                    speak('Exiting God Mode Sir.')
                    k = False
                    break
                data = ai_jarvis.ai_jarvis(prompt)
                print(data)
                speak(data)

        else:
            pass


try:
    main()
except Exception as e:
    printWithSeak(e)
    speak(' Sir ,Do you want to exit')
    check = speakInput().lower()
    if check == 'yes':
        exit(0)
    else:
        main()
