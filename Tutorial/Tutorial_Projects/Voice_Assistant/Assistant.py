import pyttsx3
# Write (pip install pyttsx3)
# at this time i am having a proble running pyttsx3 so again install
# pip install -Iv pyttsx3==2.6 -U
# the older version
import datetime
import speech_recognition as sr
# pip install speechRecognition

engine = pyttsx3.init('sapi5')
# to get the inbuild microsoft voice 
# https://en.wikipedia.org/wiki/Microsoft_Speech_API
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# voices[0] is the male voice 

""""
ERROR:
     No module named 'pyaudio': https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14
        -> to solve this problem first install you have .whl file 
            -> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
        -> according to you python version:
            -> right now my version is Python 3.9.6 so,
            -> PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
        -> and then go to download folder and write 
            -> pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
"""
def speak(audio):
    engine.say(audio)
    # here engin will say the given string
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning")
    elif hour>=12 and hour<18:
        speak("good Afternoon")
    else:
        speak("Good Evening")
    speak("i am jarvis Sir. Plese tell me how may I help you")

def takeCommand():
    """
    Taking command from the user microphone and return string output
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)
        # to listen the audio from the microphone
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        # to recognize the voice using google 
        print(f"User Said {query}\n")
    except Exception as e:
        # print(e)
        # if error occure while recognizing we will again listen
        print("Say that again please...")
        return "None"
    return query
    # return string which user Speak
if __name__=="__main__":
    # speak("hello Roman, how are you")
    # wishMe()
    takeCommand()