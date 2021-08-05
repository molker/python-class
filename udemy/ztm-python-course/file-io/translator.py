# Exercise
from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('test.txt', 'r') as my_file:
        text = my_file.read()
except FileNotFoundError as e:
    print('File not found, check file path')
else:
    translation = translator.translate(text)
    with open('test-ja.txt', 'w') as result_file:
        result_file.write(translation)
