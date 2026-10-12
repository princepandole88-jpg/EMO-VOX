# audio_engine.py - Speech-to-Text and Text-to-Speech Engine
import pyttsx3
import speech_recognition as sr

class AudioEngine:
    def __init__(self):
        self.tts = pyttsx3.init()
        self.tts.setProperty('rate', 165)
        self.recognizer = sr.Recognizer()

    def speak(self, text: str):
        print(f"EMO-VOX: {text}")
        self.tts.say(text)
        self.tts.runAndWait()

    def listen_speech(self) -> str:
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                return self.recognizer.recognize_google(audio)
            except:
                return ""


