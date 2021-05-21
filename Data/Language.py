import os
from googletrans import Translator
import google_trans_new
from gtts import gTTS
from playsound import playsound
from google_trans_new import google_translator


class Language(object):

    def __init__(self, language, sentence, assistant):
        self.__language = language
        self.__sentence = sentence
        self.__assistant = assistant

    @property
    def language_code(self):
        for code in google_trans_new.LANGUAGES:
            if self.__language == google_trans_new.LANGUAGES[code]:
                return code
        return None

    def translate(self):
        translator = google_translator()
        code = self.language_code
        if code is None:
            self.__assistant.respond("Sorry, I can't translate it to this language.")
            return
        translate_text = translator.translate(self.__sentence, lang_tgt=f'{self.language_code}')
        self.__assistant.respond_every_lang(translate_text, f'{self.language_code}')
        print(translate_text)
