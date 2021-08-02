import os, pyttsx3

import speech_recognition as sr


def takeCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready Now for your Order!')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Loding . . .")
            query = r.recognize_google(audio)
            print('the command is :', query)

        except Exception as e:
            print(e)
            print('could you please repeat again ? ')
            return "None"

        import time
        time.sleep(2)
        return query


def machineSound(audio):
    machine = pyttsx3.init()
    machine.say(audio)
    machine.runAndWait()
    

machineSound("how are you mohamed, are you happy today")
while True:
    command = takeCommands()
    if "yeah" or "yea" or "sure" or "yes" or "i hope today will be nice" or "do you think that" or " give me an advice" in command:
        machineSound("ok you should not sit on the pc too much")
        break
        
machineSound('Should i turn off the pc ?')

while True:
    command = takeCommands()

    if "exit" in command:
        machineSound("sure bye")
        break

    elif 'yes' in command:
        machineSound("it will be shutdown Now ")
        os.system("shutdown /s /t 30")

    elif "no" in command:
        machineSound("Enjoy your rest time ")