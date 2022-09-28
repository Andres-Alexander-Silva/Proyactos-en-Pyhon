import speech_recognition as sr
from pygame import mixer
import pyttsx3, pywhatkit, datetime, keyboard

name = "lina"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec

def run():
    rec = listen()
    if "reproduce" in rec:
        music = rec.replace("reproduce", "")
        print("Reproduciendo"+music)
        talk("Reproduciendo"+music)
        pywhatkit.playonyt(music)
    elif "hora" in rec:
        hora = datetime.datetime.now().strftime("%I:%M %p")
        print("Son las "+hora)
        talk("Son las "+hora)
    elif "alarma" in rec:
        num = rec.replace("alarma", "")
        num = num.strip()
        print("Alarma activada "+num+" horas")
        talk("Alarma activada "+num+" horas")
        while True:
            if datetime.datetime.now().strftime("%H:%M") == num:
                print("Despierta...")
                mixer.init()
                mixer.music.load("Despertador-de-uribe.mp3")
                mixer.music.play()
                if keyboard.read_key() == "s":
                    mixer.music.stop()
                    break

if __name__ == "__main__":
    run()