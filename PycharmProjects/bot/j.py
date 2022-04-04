import random
a=['a', 'kk', 'ab', 'ac', 'd', 'ee']
for elem in reversed(a):
    if elem[0]!='a':
        a.remove(elem)
print(a)