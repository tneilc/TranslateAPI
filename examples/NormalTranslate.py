from Translator import Translate

app = Translate()

to_translate = "Hello"
from_language = "en"
to_language = "de"

result = app.translate(to_language,from_language,to_translate)  
print(result)

#Output:
#{'From': 'en', 'To': 'de', 'Thing': 'Hello', 'Result': 'Hallo'}