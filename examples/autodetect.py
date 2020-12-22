from Translator import Translate

app = Translate()

to_translate = "Hello"
to_language = "de"

result = app.autodetect(to_language,to_translate)
print(result)

#Output:
#{'From': 'en-US', 'To': 'de', 'Thing': 'Hello', 'Result': 'Hallo'}