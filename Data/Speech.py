import speech_recognition as sr
from gtts import gTTS  # Google text to speech
from playsound import playsound  # To play sound
import os  # Save/open files


class Speech:

    @classmethod
    def talk(cls):
        input = sr.Recognizer()
        with sr.Microphone() as source:
            audio = input.listen(source)
            data = ""
            try:
                data = input.recognize_google(audio)
                print("Your question is, " + data)

            except sr.UnknownValueError:
                print("Sorry I did not hear your question, Please try again.")
        return data

    # Method to speak in english - default
    @classmethod
    def respond(cls, output):
        num = 0
        print(output)
        num += 1
        response = gTTS(text=output, lang='en')
        file = str(num)+".mp3"
        response.save(file)
        playsound(file, True)
        os.remove(file)

    # Method to speak in every language
    @classmethod
    def respond_every_lang(cls, output, lang):
        num = 0
        print(output)
        num += 1
        response = gTTS(text=output, lang=lang)
        file = str(num) + ".mp3"
        response.save(file)
        playsound(file, True)
        os.remove(file)