
import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr #Pip install speech recognition
import wikipedia #pip install wikipedia
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install pyautogui
import random 
import json
import requests
from urllib.request import urlopen
import wolframalpha #pip install wolframalpha
import time


wb.register('chrome', None, wb.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application/chrome.exe"))

engine = pyttsx3.init()
wolframalpha_app_id = "WLW5AT-82T4ALK6GV"

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

speak ("Olá usuário")

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 24 hour clock
    speak("Atualmente são: ")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("Hoje é dia ")
    speak(date)
    speak("Do mês")
    speak(month)
    speak("Do ano")
    speak(year)

def wishme():
    speak("Saudações Garots!")
    time_()
    date_()

    #Aqui vão as saudações

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <12:
        speak("Bom dia camarada!")
    elif hour >=12 and hour <18:
        speak("Boa tarde camarada!")
    elif hour >=18 and hour <24:
        speak("Boa noite camarada!")
    else:
        speak("Boa noite camarada!")

    speak("Estou a seu serviço. Por favor, diga-me como ajudá-lo hoje?")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-US")
        print(query)

    except Exception as e:
        print(e)
        print("Por favor repita... ")
        return "None"
    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak("Cpu is at"+usage)

    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def screenshot():
    img = pyautogui.screenshot()
    img.save("image1.png")
    print ("Screenshot taken!")


def joke():
    speak(pyjokes.get_joke())


if __name__ ==  "__main__":
    
    wishme()

    while True:
        query = TakeCommand().lower()

        #All commands will be stored in lower case in query
        #For easy recognition

        if "time" in query: # Tell us the time when asked
            time_()

        if "date" in query: #Tell us the date when asked
            date_()

        elif "wikipedia" in query:
            speak("Procurando....")
            query=query.replace("Wikipedia","")
            result = wikipedia.summary(query,sentences=5)
            speak("Segundo a Wikipedia...")
            print(result)
            speak(result)


        elif 'search in chrome' in query:
             speak('O que você gostaria de pesquisar?')
             search = TakeCommand().lower()

             wb.get('chrome').open_new_tab(search + '.com')

        elif "search youtube" in query:
            speak("O que eu deveria pesquisar?")
            Search_Term = TakeCommand().lower()
            speak("Lá vamos nós para o YouTube") 
            wb.open("https://www.youtube.com/results?search_query="+Search_Term)
        
        elif "search google" in query:
            speak("O que eu devo pesquisar?")
            Search_Term2 = TakeCommand().lower()
            speak("Aperte os cintos, vamos decolar rumo ao Google")
            wb.open("https://www.google.com/search?q="+Search_Term2)  ##Só funfa com palavras em inglês

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            joke()

        elif "go offline" in query:
            speak("Estou de saída, camarada!")
            quit()

        elif "microsoft word" in query:
            speak("Abrindo o word....")
            ms_word = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\Word 2016.exe"
            os.startfile(ms_word)  #Only open the folders

        elif "microsoft word premium" in query:
            speak("Abrindo o word....")
            ms_word =r"E:/Office/Office16/WINWORD.EXE"
            os.startfile(ms_word) #You need the paid version
 
        elif "write a note" in query:
            speak("O que eu deveria escrever?")
            notes = TakeCommand()
            file = open("notes.txt","w")
            speak("Devo incluir data e hora?")
            ans = TakeCommand()
            if "yes" or "sure" in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":-")
                file.write(notes)
                speak("Done Taking notes")
            else:
                file.write(notes)
        
        elif "show notes" in query:
            speak("mostrando anotações")
            file = open("notes.txt", "r")
            print(file.read())
            speak(file.read())

        elif "screenshot" in query:
            screenshot()

        elif "play music" in query:
            if "play music" in query:
                audio_1 = "E:\cr"
                audio_2 = "E:\dr"
                speak ("Which one should I choose, potato or tomato")
                ans = (TakeCommand().lower())
                while(ans!= "potato" and ans!= "tomato"):
                    speak("Tente de novo!")
                    ans = (TakeCommand().lower())
            
            if "potato" in ans:
                songs_dir = audio_1
                songs = os.listdir(songs_dir)
                print(songs)

            elif "tomato" in ans:
                songs_dir = audio_2
                songs = os.listdir(songs_dir)
                print(songs)

            speak("Select a random number")
            rand = (TakeCommand().lower())
            while("number" not in rand and rand !="random"):
                speak("I could not understand you. Please try again.")
                rand =(TakeCommand().lower())
                if "number" in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
                elif "random" in rand:
                    rand = random.randint(1,11)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
    
        elif "play song" in query:
            music_dir = "E:\dr"  
            music = os.listdir(music_dir)
            speak("What should I choose?")
            ans = TakeCommand().lower()
            no = int(ans.replace("number", ""))
            os.startfile(os.path.join(music_dir,music[no]))      


        elif "nice job" in query:
            speak("Eu vos agradeço de todo coração pelo elogio!") 
            TakeCommand().lower()

        elif "good job" in query:
            speak("Eu agradeço a você desde o fundo de meu coração")
            TakeCommand().lower()

        elif "remember that" in query:
            speak("What should I remember?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open("memory.txt","w")
            remember.write(memory)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("memory.txt","r")
            speak("You asked me to remember that"+remember.read())


        elif "where is" in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)


        elif "news" in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=445fc78a0d7a41cf9c848a78ef0b8ddb")
                data = json.load(jsonObj)
                i = 1

                speak("Here are some top headlines from the Entertainment Industry")
                print("========= Top Headlines ===========")
                for item in data["articles"]:
                    print(str(i)+". "+item["title"]+"\n")
                    print(item["description"]+"\n")
                    speak(item["title"])
                    i += 1

            except Exception as e:
                print(str(e))
            
        elif "calculate" in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index("calculate")
            query = query.split()[indx + 1:]
            res = client.query("".join(query))
            answer = next(res.results).text
            print("The answer is : "+answer)        
            speak("The answer is "+answer)


        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")


        elif "stop listening" in query:
            speak("For how many seconds do you want me to stop listening to your commands?")
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif "log out" in query:
            os.system("shutdown -1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
