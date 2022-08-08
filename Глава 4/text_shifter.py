text = str(input('Введите текст: '))
new_text = ''
for word in text[len(text):0:-1]:
    new_text += word
print(new_text + text[0])