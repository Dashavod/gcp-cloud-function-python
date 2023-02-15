
from googletrans import Translator
from dialogflow import detect_intent_texts
with open('train.txt') as f:
    lines = f.readlines()
print(lines)
translator = Translator()
translated = {translator.translate(phrase, dest="uk") for phrase in lines}
print([item.text for item in translated])
[detect_intent_texts("uk-devtorium-q-a-alek","scr5", {item.text}, "uk") for item in translated]
# for str in translated:
#     detect_intent_texts("uk-devtorium-q-a-alek", "scr", {str}, "ua")
#detect_intent_texts("devtorium-bot-e9vy", "scr", translated, "en")