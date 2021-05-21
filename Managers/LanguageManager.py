import Data.Language as l


def service_sentence(personal_assistant):
    personal_assistant.respond("To which language do you want to translate? ")
    language = personal_assistant.talk()
    while language == "":
        personal_assistant.respond("You have to give me a language to translate.")
        language = personal_assistant.talk()
    personal_assistant.respond("Tell sentence which you want to translate? ")
    sentence = personal_assistant.talk()
    while sentence == "":
        personal_assistant.respond("You have to give me a sentence to translate.")
        sentence = personal_assistant.talk()
    translator = l.Language(language.lower(), sentence, personal_assistant)
    translator.translate()
