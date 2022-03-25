import requests , json , random , pyttsx3 , datetime
import time as tm
#İmport modules

#Adjustments
jarvis = pyttsx3.init()
time=datetime.datetime.now()
an=(time.hour)
time_now =datetime.datetime.now()
now_time =time_now.strftime("%H:%M")
#Talking Function
def talk(text):
    voices = jarvis.getProperty('voices') 
    jarvis.setProperty('rate', 190)
    jarvis.setProperty('voice', voices[0].id)
    jarvis.say(text)
    jarvis.runAndWait()

tm.sleep(2)
#Startup Function

def startup():
    link= "Put Your API key here"
    response = requests.get(link)
    a = response.json()
    if a["cod"] != "404":
        b = a["weather"]
        c=b[0]["description"]
    lm = [1,2]
    answer = random.choice(lm)
    while True:
        if 6<=an<=10:
            if answer==1:
                talk(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Morning")
                print(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Morning")
            if answer==2:
                talk(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana .  Good Morning")
                print(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana .  Good Morning")
            break
        if 10<an<=19:
            if answer==1:
                talk(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Afternoon")
                print(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Afternoon")
            if answer==2:
                talk(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana . Good Afternoon")
                print(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana . Good Afternoon")
            break
        if 19<an<=22:
            if answer==1:
                talk(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Evening")
                print(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Evening")
            if answer==2:
                talk(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana . Good Evening")
                print(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana . Good Evening")
            break
        if 22<an<=24:
            if answer==1:
                talk(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Night")
                print(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Night")
            if answer==2:
                talk(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana . Good Night")
                print(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana . Good Night")
            break
        if 0<=an<6:
            if answer==1:
                talk(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Night")
                print(f"System Online! Hi again Sir! Current time is {now_time}. {c} in Adana . Good Night")
            if answer==2:
                talk(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana . Good Night")
                print(f"System Online! Welcome Sir! Current time is {now_time}. {c} in Adana . Good Night")
            break
        
        else:
            talk("System Online! Hi again Sir! Good To See You")
            print("System Online! Hi again Sir! Good To See You")
            break



startup()

"""
Basic Jarvis Startup project by Enes Duran
"""
