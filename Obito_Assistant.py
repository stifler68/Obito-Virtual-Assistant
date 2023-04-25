import cv2
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyjokes
import ctypes
import time
import smtplib
import requests
import pyautogui
import psutil
import wolframalpha
import screen_brightness_control as sbc
from selenium import webdriver

from tkinter import *
import tkinter.font as font
from PIL import ImageGrab, ImageTk, Image

window = Tk()
window.title("Virtual Assistant")
# getting screen width and height of display
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
# setting tkinter window size
window.geometry("%dx%d" % (width, height))
# window.configure(bg='red')

try:
   //  get wolframeallpha api key from there website and add on below line
    app = wolframalpha.Client("Q539P8-JWLJU")
except Exception:
    print('some feature are not working')

emails = {
    "Parab": "sample123@gmail.com",
    "Ravi": "helloworld@gmail.com"
}

city = "mumbai"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # path of chrome

# speech to text
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon Sir!")
    else:
        speak("Good Evening Sir!")

    name = ("how may i help you")
    speak("I am your Personal Assistant")
    speak(name)


def takeCommand():
    """ Its take input from microphone and return in string type """

    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listining...")
        Output.insert(END, 'Listining...' + '\n')
        window.update()
        r.energy_threshold = 800
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.3)

        audio = r.listen(source, phrase_time_limit=5)
        try:
            print("Recognization...")
            Output.insert(END, 'Recognization...' + '\n')
            window.update()
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}\n")
            Output.insert(END, 'User said -> ' + query + '\n')
            window.update()
        except Exception as e:
            print("Say it again ")
            Output.insert(END, 'Say it again ' + '\n')

            time.sleep(2)
            Output.delete("1.0", "end")
            window.update()
            return "None"

    time.sleep(2)
    Output.delete("1.0", "end")
    window.update()
    return query


def Increase_brightness():
    try:
        currrent_brightness = sbc.get_brightness()
        if (currrent_brightness == 100):
            speak("brightness is already full")
        else:
            increased_brightness = currrent_brightness + 10
            sbc.set_brightness(increased_brightness)
            if (currrent_brightness != 100):
                speak("sir should i increase the brightness or its good")
    except Exception as e:
        speak("sir brightness is full")


def Decrease_brightness():
    try:
        currrent_brightness = sbc.get_brightness()
        if (currrent_brightness == 0):
            speak("brightness is already low")
        else:
            decreased_brightness = currrent_brightness - 10
            sbc.set_brightness(decreased_brightness)
            if (currrent_brightness != 0):
                speak("sir should i decrease the brightness or its good")
    except Exception as e:
        speak("sir brightness is low")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage + "Percentage")


def howareyou():
    query = takeCommand()
    if 'am also good' in query or 'am also fine' in query or 'healthy' in query or 'fine' in query or 'good and you' in query or 'I am also good' in query or 'I am also fine' in query or 'I am good' in query:
        speak("wow nice to know!! can i do something for you")
        query = takeCommand()
        if 'yes' in query or 'yeah sure' in query or 'yes please' in query:
            speak('okay sir tell me')
        elif 'no' in query:
            speak('okay sir')
        if 'and you obito' in query or 'and you' in query or 'what about to you' in query or 'and what about to you' in query:
            speak(" and i am also good sir")
    if 'not fine' in query or 'not well' in query or 'not good' in query or 'felling low' in query or 'not in mood' in query:
        speak("sad to hear that sir, how may I change your mood, May i play music for You?")
        query = takeCommand()
        if 'ok' in query or 'sure' in query or 'hmm' in query or 'alright' in query or 'yeah' in query or 'play music' in query:
            speak('ok sir playing music for you')
            music_dir = 'C:\\Users\\multi\\Music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            for songs in songs:
                if songs.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs))
        elif "no" in query or "it's ok" in query or "don't play" in query or 'nope' in query:
            speak("Ok sir as You like!")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("Your-email-ID@gmail.com", "Your-password")
    server.sendmail("your-email-ID@gmail.com", to, content)
    server.close()


def code():
    window.update()

    wishMe()

    global sleep_and_wake
    sleep_and_wake = " "
    while True:
        query = takeCommand().lower()

        # To sleep and wake (if else)
        if (sleep_and_wake == "sleep"):
            if ("wake up" in query):
                sleep_and_wake = "wake up"
            else:
                query = " "

        # Logic for executing tasks based on query
        if 'wikipedia' in query or 'details about' in query or 'tell me about' in query or 'who is' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            query = query.replace("details about", "")
            query = query.replace("tell me about", "")
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)



        elif 'where is' in query or 'obito where is' in query:
            query = query.replace("where is", "")
            query = query.replace("obito where is", "")
            location = query
            speak('Just a second sir, showing you were is' + location)
            url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get(chrome_path).open(url)

        elif "sleep obito" in query or "sleep" in query:
            sleep_and_wake = "sleep"
            speak("okay sir!! i am going to sleep, wake me up when you want me")

        elif "wake up" in query or "wake up obito" in query or 'hyy obito' in query:
            if (sleep_and_wake == "wake up"):
                sleep_and_wake = " "
                wishMe()
            elif (sleep_and_wake == " "):
                if ('hyy obito' in query):
                    speak("hello sir i am waken all the time for you")
                else:
                    speak("i am already waken up sir !! ")

        # To open Webcam
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        # elif "email to parab" in query:
        #     email_var = False
        #     try:
        #         speak("What should i say ")
        #         content = takeCommand()
        #         to = "jayramparab1997@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has sent ! ")
        #     except Exception as e:
        #         speak("Sorry i cant sent email there is some technical error")
        #         print(e)
        #
        # elif "email to ravi" in query:
        #     email_var = False
        #     try:
        #         speak("What should i say ")
        #         content = takeCommand()
        #         to = "cravisingh64@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has sent ! ")
        #
        #     except Exception as e:
        #         speak("Sorry i cant sent email there is some technical error")
        #         print(e)

        elif "battery status" in query or 'check battery status' in query or 'check my battery status' in query:
            battery = psutil.sensors_battery()
            percent = str(battery.percent)
            plugged = battery.power_plugged
            # plugged = "Plugged In" if plugged else "Not Plugged In"
            if plugged:
                plug = 'plugged'
            else:
                plug = 'not plugged'
            per = int(percent)
            # plugged = "Plugged In" if plugged else "Not Plugged In"
            if plugged:
                plug = "plugged"
            else:
                plug = "not_plugged"

            if plug == 'not_plugged' and per <= 30:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir please pluggin your charger because your battery is low ")
            elif plug == 'plugged' and battery > 20:
                speak("Sir your battery is ")
                speak(percent)
            elif plug == 'not_plugged' and per > 20:
                speak("Sir your battery is ")
                speak(percent)
            elif plug == 'plugged' and battery <= 20:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir your battery is low dont remove your charger")
            elif plug == 'plugged' and battery == 100:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir your battery is full please remove charger ")
            else:
                print(percent)

        elif "increase the brightness" in query or "yes increase the brightness" in query or "increase brightness" in query:
            Increase_brightness()

        elif 'increase full brightness' in query :
            currrent_brightness = sbc.get_brightness()
            bright=100-currrent_brightness
            increased_brightness = currrent_brightness + bright
            sbc.set_brightness(increased_brightness)

        elif 'decrease full brightness' in query :
            currrent_brightness = sbc.get_brightness()
            increased_brightness = 0
            sbc.set_brightness(increased_brightness)

        elif "decrease the brightness" in query or "yes decrease the brightness" in query or "decrease brightness" in query:
            Decrease_brightness()

        elif ("powers" in query or "help" in query
              or "features" in query or 'what can you do' in 'what can you do for us' in query):
            features = ''' i can help to do lot many things like..
                           i can tell you the current time and date,
                           i can tell you the current weather,
                           i can tell you battery and cpu usage,
                           i can shut down or logout or hibernate your system,
                           i can tell you non funny jokes,
                           i can open any website,
                           i can repeat what you you told me,
                           i can search the thing on wikipedia,
                           i have a wake word detection i will be online if you say hey obito
                           And yes one more thing, My boss is working on this system to add more features...,
                           tell me what can i do for you??
                           '''
            speak(features)

        if 'repeat' in query:
            query = query.replace("repeat", "")
            query = query.replace("that", "")
            speak(query)

        elif 'check my internet connection' in query or 'am I connected to internet' in query:
            hostname = "google.co.in"
            response = os.system("ping -c 1" + hostname)
            if response == 0:
                speak("Sir Internet is disconnected")
            else:
                speak("sir you are connected to internet")

        elif 'next window' in query or 'switch back' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("window switched")

        elif 'previous window' in query or 'last window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            speak("anything else sir?")

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            speak("which one")
            query = takeCommand()
            if 'next' in query:
                pyautogui.press("right")
                pyautogui.keyUp("alt")
                speak('window switched')
            if "don't switch" in query or 'go back' in query:
                pyautogui.press("left")
                pyautogui.keyUp("alt")
                speak("window switched")

        elif 'close current window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            pyautogui.keyUp("alt")

        elif 'minimise this window' in query or 'minimize current window' in query or 'minimize this' in query or 'minimize current window' in query or 'minimize the screen' in query:
            pyautogui.keyDown("win")
            pyautogui.press("down")
            pyautogui.keyUp("win")
            speak("Current window has been minimized")

        elif 'minimize all windows' in query or 'minimise all' in query or 'minimize all' in query or 'minimize all' in query:
            try:
                os.system('''powershell -command "(new-object -com shell.application).minimizeall()"''')
                speak("all windows minimized")
            except Exception as e:
                speak("Sir there are no windows to minimize")

        elif 'maximize window' in query or 'fullscreen' in query or 'maximise window' in query or 'maximise' in query:
            try:
                pyautogui.keyDown("win")
                pyautogui.press("up")
                pyautogui.keyUp("win")
                speak("This window is now on fullscreen")
            except Exception as e:
                speak("No windows to maximize")


        elif 'date' in query:
            date()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")


        # elif 'search' in query:
        #     query = query.replace("search", "")
        #     query = query.replace("obito", "")
        #     url = f"https://www.google.com/search?q={query}"
        #     webbrowser.get().open(url)
        #     speak("Here is what I got form search result" + query)

        elif "search in google" in query or "search on google" in query:
            try:
                speak("What should i search sir ")
                search_results = takeCommand()
                speak("its take some time sir ")
                driver = webdriver.Chrome(
                    executable_path='C:\\Users\\ravi singh\\Downloads\\chromedriver.exe')  # chrome drive path
                driver.get("https://google.com/")
                search = driver.find_element_by_name("q")  # name of div class in google inspect
                search.send_keys(search_results)
                time.sleep(4)
                button = driver.find_element_by_name("btnK").click()
            except Exception as e:
                speak("some error occure")

        elif 'open youtube' in query:
            # webbrowser.open('youtube.com')
            webbrowser.get(chrome_path).open('youtube.com')
            speak("Opening Youtube Sir")

        # elif 'open youtube' in query:
        #     speak('Ok sir Opening Youtube')
        #     webbrowser.open("https://youtube.com/")
        #     speak("Sir what would u like to Watch on youtube?")
        #     query = takeCommand()
        #     if 'search' in query:
        #         query = query.replace("search", "")
        #         url = f"https://www.youtube.com/results?search_query={query}"
        #         webbrowser.open(url)
        #         speak("I've searched for" + query + "in youtube")
        #     if 'will do it myself' in query or 'leave it' in query or 'no':
        #         speak("As You like sir!")




        elif 'recently closed tabs' in query or 'recently closed tabs' in query:
            try:
                pyautogui.keyDown("ctrl")
                pyautogui.keyDown("shift")
                pyautogui.press("T")
                pyautogui.keyUp("ctrl")
                pyautogui.keyUp("shift")
                speak("Recently closed tabs has been opened")
            except Exception as e:
                speak("No recent tabs found")

        elif 'open chrome' in query:
            try:
                speak('opening chrome')
                codepath = "chrome.exe"
                os.startfile(codepath)
            except Exception as e:
                speak("Chrome Not found")


        elif 'open google' in query:
            webbrowser.get(chrome_path).open('google.com')

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
            speak('chrome has been closed')


        elif 'play music' in query:
            # music_dir = 'C:\\Users\\multi\\Music'
            music_dir = 'C:\\Users\\ravi singh\\Music\\audios'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            for songs in songs:
                if songs.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs))



        elif 'joke' in query or 'make me laugh' in query:
            speak(pyjokes.get_joke())

        elif 'who made you' in query or 'who created you' in query:
            speak("I have been created by Ravisingh chauhan ")

        elif 'calculate' in query:
            # G7WRHU-5HR5ERA98H
            app_id = "G7WRHU-5HR5ERA98H"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "open website" in query:
            speak("Tell me the name of the website")
            search = takeCommand().lower()
            speak('Opening' + search)
            url = 'www.' + search + '.com'
            webbrowser.open(url)


        elif 'weather of' in query or 'current weather' in query or 'tell me current weather' in query:
            api_key = "0bf38c445cb8545f237f2d0ce54511ee"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            if 'current weather' in query or 'tell me current weather' in query:
                city_name = "mumbai"
            else:
                # query = query.replace("weather of", "")
                city_name = "mumbai"
            speak("weather of" + city_name + "is")
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'email' in query :
            try:
                speak("Whom U would like to send email")
                name = takeCommand()
                print(name)
                to = emails[name]
                speak("What should i say?")
                content = takeCommand()
                speak("Confirm, yes or no")
                mailconfig = takeCommand()
                flag = 0
                while flag != 1:
                    if "yes" in mailconfig:
                        sendEmail(to, content)
                        speak("Email has been sent succesfully")
                        flag = 1
                    elif "no" in mailconfig:
                        speak("Ok sir request has been cancelled")
                        break
                    else:
                        speak("Unable to confirm, please say again")
                        break
            except Exception as e:
                speak("Could not send email")

        elif 'lock window' in query or 'lock the system' in query:
            try:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
            except Exception as e:
                speak("Sir windows is already locked")


        elif 'cpu usage' in query or 'cpu uses' in query or 'check my cpu' in query:
            cpu()


        elif "take a screenshot" in query or "take screenshot" in query:
            snapshot = ImageGrab.grab()
            drive_letter = "C:\\Users\\ravi singh\\PycharmProjects\\Screenshot\\"
            folder_name = r'downloaded-files'
            folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
            extention = '.jpg'
            folder_to_save_files = drive_letter + folder_name + folder_time + extention
            snapshot.save(folder_to_save_files)
            speak("done sir")

        elif 'how are you' in query or 'how are you doing' in query:
            speak("am fine sir, what about you?")
            howareyou()

        elif 'hello obito' in query or 'hello' in query:
                speak("hello sir how are you!!")
                howareyou()

        elif 'goodbye obito' in query or 'see you obito' in query or 'obito down' in query or 'obito shutdown' in query or 'bye obito' in query:
            speak("Do You want me to shutdown")
            qu = takeCommand()
            if 'no' in qu or 'cancel' in qu:
                speak("Process cancelled")
            if 'yes' in qu or 'yep' in qu or 'shutdown' in qu:
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 18:
                    speak("Have a Nice day sir!")
                    exit()
                elif hour >= 18 and hour < 24:
                    speak("Ok, good Night sir")
                    exit()
                    window.destroy()

        elif "close app" in query or "stop working" in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 18:
                speak("okay sir! Have a Nice day sir!")
                exit()
            elif hour >= 18 and hour < 24:
                speak("Ok, good Night sir")
                exit()
                window.destroy()
            window.destroy()
            exit()

        # Delete the GUI Contain
        # time.sleep(2)
        # Output.delete("1.0", "end")


if __name__ == "__main__":
    load = Image.open(r"res/1 (1).png")
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render)
    img.place(x=420, y=45)

    myFont = font.Font(family=' sans-serif', size=14)
    Output = Text(window, height=8, width=40, bg="light cyan", font=myFont)

    # scroll_bar = Scrollbar(window)
    # scroll_bar.pack(side=RIGHT)
    Output.pack(side=LEFT)
    Output.place(x=420, y=300)

    # Output.bind("<Key>", lambda a: "break")

    code()

window.mainloop()
