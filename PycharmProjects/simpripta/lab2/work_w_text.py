f = open('text.txt', encoding = "UTF-8")
text = f.read()
symbols = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя '
text = text.lower()
for i in text:
    if i not in symbols:
        text = text.replace(i, '')
f.close()
t=open('text.txt','w',encoding = "UTF-8")
t.write(text)