arr=['а','б','в','г','ґ','д','е','є','ж','з','и','і','ї', 'й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ю','я']
string='евьчфтклйтмщюзбіґхґщсьтмі'
dict_alph={}
for elem in arr:
    dict_alph[elem]=arr.index(elem)


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"
print (dict_alph)
dict_cypher={}
for elem in string:
    dict_cypher[elem]=dict_alph[elem]
print(dict_cypher)
result=''

for k in range (1,len(string)):
    for t in range(k,len(string)):
        x=dict_cypher[string[t]]-dict_cypher[string[t-k]]
        if x<0:
            x+=33
        res=get_key(x,dict_alph)
        result+=res
    print(result)
    result=''