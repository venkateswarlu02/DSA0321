from googletrans import Translator

def translate_text(text, src_lang="en", tgt_lang="fr"):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=tgt_lang)
    return translation.text

text = "Hello, how are you,my name is kannan,have you had your lunch?"
print(translate_text(text, src_lang="en", tgt_lang="fr"))
