import pyttsx3
import speech_recognition as sr
import eel
import time
import os
import sys
import smtplib
from email.message import EmailMessage
import pywhatkit                                   # pip install pywhatkit
#import MyAlarm      
import math
import datetime 

import speech_recognition as sr                    # pip install SpeechRecognition
import pyaudio                                   # pip install pipwin and then pipwin install pyaudio
import wikipedia                                   # pip install wikipedia
import webbrowser   
#import ecapture as ec                
import pyjokes                                     
#from speedtest import Speedtest                    # pip install speedtest-cli
from pywikihow import search_wikihow               # pip install pywikihow
import pyautogui                                   # pip install pyAutoGUI
import poetpy                                      # pip install poetpy
import random
from forex_python.converter import CurrencyRates   # pip install forex-python
import requests                                    # pip install requests
import bs4        

from engine.saveChat import *                                 # pip install beautifulsoup4

import wolframalpha                                # pip install wolframalpha
from quote import quote                            # pip install quote
# import winshell as winshell                        # pip install winshell
# from geopy.geocoders import Nominatim              # pip install geopy  and pip install geocoder
# from geopy import distance
import turtle
import random
#import snake_game
#import screen_record
import requests
from PIL import Image


engine = pyttsx3.init()

def fun_talk(audio):
    engine.say(audio)
    engine.runAndWait()

def get_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1

        audio = rec.listen(source)

        try:
            print("Recognizing...")
            query = rec.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "None"
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None"

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query





def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
    chathistory.save_to_mongo()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)

        # function code from first bot 
        elif 'search' in query:
            query = query.replace('search', '')
            pywhatkit.search(query)

        elif 'set alarm' in query:
            fun_talk("alarm set for 3 PM")
            a_info = get_command()
            a_info = a_info.replace('set an alarm for', '')
            a_info = a_info.replace('.', '')
            a_info = a_info.upper()
         #   MyAlarm.alarm(a_info)

        elif 'exit p a' in query:
            fun_talk("Exiting Sir...")
            sys.exit()

        elif 'price of' in query:
            query = query.replace('price of', '')
            query = "https://www.amazon.in/s?k=" + query[-1] #indexing since I only want the keyword
            webbrowser.open(query)

        elif 'poem' in query:
            fun_talk('Poem of which author you want to listen?')
            auth = get_command()
            poem = poetpy.get_poetry('author', auth, 'title,linecount') 
            poems = poetpy.get_poetry('author', auth, 'lines')  

            poem_len = len(poem)
            # print(poem_len)
            poem_no = random.randint(1, poem_len)
            print("Title- ", poem[poem_no]['title'])
            fun_talk(f"Title- {poem[poem_no]['title']}")
            print("No. of lines-", poem[poem_no]['linecount'])
            fun_talk(f"No. of lines- {poem[poem_no]['linecount']}")
            poem_str = '\n'
            print("Poem-\n", poem_str.join(poems[poem_no]['lines']))
            fun_talk(f"Poem-\n {poem_str.join(poems[poem_no]['lines'])}")

        elif 'weather' in query or 'temperature' in query:
            try:
                fun_talk("Tell me the city name.")
                city = get_command()
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=eea37893e6d01d234eca31616e48c631"
                w_data = requests.get(api).json()
                weather = w_data['weather'][0]['main']
                temp = int(w_data['main']['temp'] - 273.15)
                temp_min = int(w_data['main']['temp_min'] - 273.15)
                temp_max = int(w_data['main']['temp_max'] - 273.15)
                pressure = w_data['main']['pressure']
                humidity = w_data['main']['humidity']
                visibility = w_data['visibility']
                wind = w_data['wind']['speed']
                sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
                sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

                all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
                all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
                fun_talk(f"Gathering the weather information of {city}...")
                print(f"Gathering the weather information of {city}...")
                print(all_data1)
                fun_talk(all_data1)
                print(all_data2)
                fun_talk(all_data2)

            except Exception as e:
                pass

        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                fun_talk(month)

            tell_month()

        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                fun_talk(day)

            tell_day()

        elif "calculate" in query:
            try:
                app_id = "JUGV8R-RXJ4RP7HAG"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                fun_talk("The answer is " + answer)

            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")


        elif 'weather' in query or 'temperature' in query:
            try:
                fun_talk("Tell me the city name.")
                city = get_command()
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=eea37893e6d01d234eca31616e48c631"
                w_data = requests.get(api).json()
                weather = w_data['weather'][0]['main']
                temp = int(w_data['main']['temp'] - 273.15)
                temp_min = int(w_data['main']['temp_min'] - 273.15)
                temp_max = int(w_data['main']['temp_max'] - 273.15)
                pressure = w_data['main']['pressure']
                humidity = w_data['main']['humidity']
                visibility = w_data['visibility']
                wind = w_data['wind']['speed']
                sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
                sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

                all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
                all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
                fun_talk(f"Gathering the weather information of {city}...")
                print(f"Gathering the weather information of {city}...")
                print(all_data1)
                fun_talk(all_data1)
                print(all_data2)
                fun_talk(all_data2)

            except Exception as e:
                pass

        elif 'month' in query or 'month is going' in query:
            def tell_month():
                month = datetime.datetime.now().strftime("%B")
                fun_talk(month)

            tell_month()

        elif 'day' in query or 'day today' in query:
            def tell_day():
                day = datetime.datetime.now().strftime("%A")
                fun_talk(day)

            tell_day()




        elif 'send email' in query:
    
            def send_mail(receiver, subject, message):

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('your_email@something.com', 'your_password')

                email = EmailMessage()
                email['From'] = 'your_email@something.com'
                email['To'] = receiver
                email['Subject'] = subject
                email.set_content(message)
                server.send_message(email)


            email_list = {
                'Umesh': 'ums945891@gmail.com',
                'Rishabh': 'rishabhran123@gmail.com',
                'name': 'something@something.com',
                'assitant': 'something@something.com'
            }


            def get_mail_info():
                fun_talk('To whom you want to send email')
                name = get_command()
                receiver = email_list[name]
                print(receiver)
                fun_talk('What is the subject of your email?')
                subject = get_command()
                fun_talk('Tell me the text in your email')
                message = get_command()

                send_mail(receiver, subject, message)

                fun_talk(' Your email is sent Successfully.')

        
                send_more = get_command()
                if 'yes' in send_more:
                    get_mail_info()


            get_mail_info()    

        elif "calculate" in query:
            try:
                app_id = "JUGV8R-RXJ4RP7HAG"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                fun_talk("The answer is " + answer)

            except Exception as e:
                print("Couldn't get what you have said, Can you say it again??")

            #459
        elif 'what' in query or 'who' in query:  # or 'where' in query:  
            
            client = wolframalpha.Client("JUGV8R-RXJ4RP7HAG")
            res = client.query(query)
            try:
                print(next(res.results).text)
                fun_talk(next(res.results).text)

            except StopIteration:
                print("No results found!!")    

        elif 'write a note' in query or 'make a note' in query:
            fun_talk("What should I write, sir??")
            note = get_command()
            file = open('Notes.txt', 'a')
            fun_talk("Should I include the date and time??")
            n_conf = get_command()
            if 'yes' in n_conf:
                str_time = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(str_time)
                file.write(" --> ")
                file.write(note)
                fun_talk("Point noted successfully.")
            else:
                file.write("\n")
                file.write(note)
                fun_talk("Point noted successfully.")        

        elif 'how to' in query:
            try:
                # query = query.replace('how to', '')
                max_results = 1
                data = search_wikihow(query, max_results)
                # assert len(data) == 1
                data[0].print()
                fun_talk(data[0].summary)
            except Exception as e:
                fun_talk('Sorry, I am unable to find the answer for your query.')
                        
        elif 'news' in query or 'news headlines' in query:
            url = "https://news.google.com/news/rss"
            client = webbrowser(url)
            xml_page = client.read()
            client.close()
            page = bs4.BeautifulSoup(xml_page, 'xml')
            news_list = page.findAll("item")
            fun_talk("Today's top headlines are--")
            try:
                for news in news_list:
                    print(news.title.text)
                    # print(news.pubDate.text)
                    fun_talk(f"{news.title.text}")
                    # fun_talk(f"{news.pubDate.text}")
                    print()

            except Exception as e:
                fun_talk('Sorry, I am unable to find the answer for your query.')
                # pass





        
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)
        else:
            from engine.features import chatBot
            chatBot(query)
    except:
        print("error")
    
    eel.ShowHood()