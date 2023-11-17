import speech_recognition as sr
import win32com.client

# Here we import the os, which we will utilize for PyAudio speaking
import os

# We have installed & imported this package to allow 'text-to-speech' feature
import pyttsx3

# this module will be helpful for doing task with Jarvis
import webbrowser as wb

# for ai
import openai

# for users music path play
import subprocess
import sys

# for dates and time
import datetime


def say(text):
    engine = pyttsx3.init()  # used here for the initialization
    engine.say(text)
    engine.runAndWait()


def takeCommand():  # this function here is for our code to recognize the users inputs
    r = sr.Recognizer()
    with sr.Microphone() as source:  # here we are taking voice inputs from the users mic
        r.pause_threshold = 1
        audio = r.listen(source)  # this listens to our mics input

        # We are implementing the 'try', simply exceptional handling
        try:
            # now this recognize_<browser>, puts the users voice as an input in Google search, in language Eng IND
            # remember we can assign any browsers
            query = r.recognize_google(audio, language="en-in")

            # now print
            print(f"User said: {query}")
            # return the query , this will allow the function to repeat what we said
            return query
        except Exception as e:
            return "Error occurred. Sorry"

#📌📌creating a 'chat' function which will use AWS developed 'code whisperer', which will auto suggests us code etc
# def chat(query):
# # write any questions and whisperer will suggest it
#     #we can resume it anytime we want.


if __name__ == '__main__':
    print('PyCharm')

    # Here now we call the 'say' function to say
    say("Hello & Namaste, I am JARVIS A I!")

    # now we will run the function take command here & store the command as the text form and after will ask Jarvis
    # to say it
    while True:
        print("Listening...")
        query = takeCommand()
        # here we are giving sites names and their correspoding web links, this will allow us to open the sites
        # sites = [["google", "https://google.com"], ["youtube","https://youtube.com"],
        #          ["V TOP","https://vtop2.vitap.ac.in/vtop/initialProcess"]]
        sites = {"google": "https://www.google.com", "youtube": "https://www.youtube.com",
                 "VIT AP student site": "https://vtop2.vitap.ac.in/vtop/initialProcess"}
        # running for loop to traverse
        for site_name, site_link in sites.items():
            if f"open {site_name}".lower() in query.lower():
                say(f"Opening {site_name}, please wait")
                wb.open(site_link)
                break

        # Now will ask to open music for us by mentioning its system address
        if "open music" in query.lower():
            musicPath = r"C:\Users\ppuri\Music\Mercy-(Mr-Jatt.com).mp3"
            if sys.platform == "darwin":
                os.system(f"open {musicPath}")
            elif sys.platform == "win32":
                os.startfile(musicPath)
            else:
                opener = "open" if os.path.exists("/usr/bin/xdg-open") else "open"
                subprocess.call([opener, musicPath])
        else:
            print("Music file not found.")

        # asking time from Jarvis
        if "the time" in query.lower():
            strFTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir/Mam the time is {strFTime}")

        # here Jarvis will be able to open apps for us just by mentioning the name of it
        # running for loop to traverse
        # for app_name, app_path in apps.items():
        #     if f"open {app_name}".lower() in query.lower():
        #         say(f"Opening {app_name}, please wait")
        #         os.system(app_path)

        # Bro this section sucks bro 🙁
        # But after one day it worked dude 😉, just find the files/apps location in Program files or x86
        apps = {"Chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                "Brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
                "Media player": r"C:\Program Files\Windows Media Player\wmplayer.exe",
                "Epic games": r"C:\Program Files (x86)\Epic Games\Epic Online Services\EpicOnlineServices.exe",

                }

        for app_name, app_path in apps.items():
            if f"open {app_name.lower()}".lower() in query.lower():
                try:
                    # subprocess.Popen([app_path])
                    say(f"Opening {app_name}, please wait")
                    os.startfile(app_path)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    say("Sorry, I am unable to open the application.")
                break

        apps = {
            "calculator": "calc",
            "notepad": "notepad",
            "spotify":"spotify"
            # Add more applications with their names as needed
        }

        for app_name, app_command in apps.items():
            if f"open {app_name.lower()}".lower() in query.lower():
                try:
                    os.system(f"start {app_command}")
                    say(f"Opening {app_name}, please wait")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    say("Sorry, I am unable to open the application.")
                break
