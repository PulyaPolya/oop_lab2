import math
alpSpace = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
alpWSpace = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

f = open('sm', encoding = "UTF-8")
text = f.read()
for i in text:
    if i.isupper():
        i = i.lower()
    if i not in alpSpace:
        text = text.replace(i, '')


MonoDick = dict()
for a in alpSpace:
    MonoDick[a] = 0

for i in text:
    MonoDick[i] = MonoDick[i] + 1

count = len(text)

for i in MonoDick:
    MonoDick[i] = MonoDick[i] / count

BiDick = dict()
for i in alpSpace:
    for j in alpSpace:
        word = i + j
        BiDick[word] = 0

for j in range(0, count-1, 1):
    if text[j] + text[j + 1] in BiDick:
        BiDick[text[j] + text[j + 1]] += 1
for i in BiDick:
   BiDick[i] = BiDick[i] / count
def count_H(Dick,n):
    H=0
    for elem in Dick:
        if Dick[elem]!=0.0:
            H=H-Dick[elem]*math.log(2,Dick[elem])
            print(Dick[elem],H, elem)
    return H/n
#print(count_H(MonoDick,1))
print( BiDick)
#print(count_H(BiDick,2))
k=0
for elem in BiDick:
    k+=BiDick[elem]
print(k)
f.close()
t=open('text','w',encoding = "UTF-8")
t.write(text)
t.close()