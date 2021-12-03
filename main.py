from greets import greetings
from translate import Translator

translator = Translator(to_lang='de')
print(translator.translate("hello"))

for g in greetings:
    print(translator.translate("hello"))
    print(g)
